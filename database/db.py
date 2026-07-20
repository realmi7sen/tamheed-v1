import sqlite3
from pathlib import Path
from contextlib import contextmanager
import hashlib
from typing import Optional
from datetime import datetime


class TamheedDB:
    """طبقة قاعدة البيانات SQLite — كاش، استخدام يومي، محادثات."""

    def __init__(self, db_path: str = "tamheed.db"):
        self.db_path = Path(db_path)
        self._ensure_schema()

    def _ensure_schema(self):
        """إنشاء الجداول إذا ما كانت موجودة."""
        with self.connection() as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS cache (
                    key TEXT PRIMARY KEY,
                    response TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS user_usage (
                    user_id INTEGER PRIMARY KEY,
                    day INTEGER NOT NULL,
                    count INTEGER DEFAULT 0,
                    last_message_ts REAL DEFAULT 0
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS conversations (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    role TEXT NOT NULL,
                    content TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS videos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    section TEXT NOT NULL,
                    topic TEXT NOT NULL,
                    message_id TEXT NOT NULL,
                    telegram_link TEXT,
                    published_week INTEGER,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.execute("""
                CREATE TABLE IF NOT EXISTS media_log (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id INTEGER NOT NULL,
                    media_type TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            """)
            conn.commit()

    @contextmanager
    def connection(self):
        """Context manager للاتصال — يفتح وإغلق تلقائي."""
        conn = sqlite3.connect(str(self.db_path))
        conn.row_factory = sqlite3.Row
        try:
            yield conn
        finally:
            conn.close()

    # ===== CACHE =====
    def cache_get(self, key: str) -> Optional[str]:
        """استرجاع رد مخزّن من الكاش."""
        with self.connection() as conn:
            row = conn.execute(
                "SELECT response FROM cache WHERE key = ?", (key,)
            ).fetchone()
            return row["response"] if row else None

    def cache_set(self, key: str, response: str) -> None:
        """خزّن رد في الكاش."""
        with self.connection() as conn:
            conn.execute(
                "INSERT OR REPLACE INTO cache (key, response) VALUES (?, ?)",
                (key, response),
            )
            conn.commit()

    def cache_clear_old(self, days: int = 7) -> int:
        """احذف cache أقدم من N أيام."""
        with self.connection() as conn:
            cursor = conn.execute(
                """
                DELETE FROM cache 
                WHERE created_at < datetime('now', '-' || ? || ' days')
                """,
                (days,),
            )
            conn.commit()
            return cursor.rowcount

    # ===== USAGE (الحد اليومي) =====
    def usage_get(self, user_id: int, day: int) -> dict:
        """استرجع عداد اليوم — إذا اليوم تغيّر نعتبر العدّاد صفر."""
        with self.connection() as conn:
            row = conn.execute(
                "SELECT day, count, last_message_ts FROM user_usage WHERE user_id = ?",
                (user_id,),
            ).fetchone()
            if row and row["day"] == day:
                return {"count": row["count"], "last_message_ts": row["last_message_ts"]}
            # يوم جديد أو مستخدم جديد
            return {"count": 0, "last_message_ts": row["last_message_ts"] if row else 0.0}

    def usage_increment(self, user_id: int, day: int, ts: float) -> None:
        """زد العدّاد لليوم الحالي، أو صفّره لو اليوم تغيّر."""
        with self.connection() as conn:
            existing = conn.execute(
                "SELECT day FROM user_usage WHERE user_id = ?",
                (user_id,),
            ).fetchone()

            if existing is None:
                conn.execute(
                    "INSERT INTO user_usage (user_id, day, count, last_message_ts) VALUES (?, ?, 1, ?)",
                    (user_id, day, ts),
                )
            elif existing["day"] != day:
                conn.execute(
                    "UPDATE user_usage SET day = ?, count = 1, last_message_ts = ? WHERE user_id = ?",
                    (day, ts, user_id),
                )
            else:
                conn.execute(
                    "UPDATE user_usage SET count = count + 1, last_message_ts = ? WHERE user_id = ?",
                    (ts, user_id),
                )
            conn.commit()

    # ===== CONVERSATIONS (الذاكرة) =====
    def conversation_add(self, user_id: int, role: str, content: str) -> None:
        """أضف رسالة للمحادثة (user أو assistant)."""
        with self.connection() as conn:
            conn.execute(
                "INSERT INTO conversations (user_id, role, content) VALUES (?, ?, ?)",
                (user_id, role, content),
            )
            conn.commit()

    def conversation_get_recent(self, user_id: int, limit: int = 6) -> list:
        """استرجع آخر N رسالة لمستخدم (للذاكرة)."""
        with self.connection() as conn:
            rows = conn.execute(
                """
                SELECT role, content FROM conversations 
                WHERE user_id = ? 
                ORDER BY created_at DESC 
                LIMIT ?
                """,
                (user_id, limit),
            ).fetchall()
            # عكس الترتيب (الأقدم أولاً)
            return [{"role": row["role"], "content": row["content"]} for row in reversed(rows)]

    def conversation_clear_old(self, user_id: int, keep_count: int = 50) -> None:
        """احذف محادثات قديمة — احتفظ بـ N رسالة الأخيرة فقط."""
        with self.connection() as conn:
            conn.execute(
                """
                DELETE FROM conversations 
                WHERE user_id = ? AND id NOT IN (
                    SELECT id FROM conversations 
                    WHERE user_id = ? 
                    ORDER BY created_at DESC 
                    LIMIT ?
                )
                """,
                (user_id, user_id, keep_count),
            )
            conn.commit()

    # ===== VIDEOS (للمستقبل) =====
    def video_get_by_section(self, section: str) -> Optional[dict]:
        """ابحث عن مقطع بالموضوع."""
        with self.connection() as conn:
            row = conn.execute(
                "SELECT * FROM videos WHERE section = ?",
                (section,),
            ).fetchone()
            return dict(row) if row else None

    def video_add(
        self,
        section: str,
        topic: str,
        message_id: str,
        telegram_link: Optional[str] = None,
        published_week: Optional[int] = None,
    ) -> None:
        """أضف مقطع جديد."""
        with self.connection() as conn:
            conn.execute(
                """
                INSERT INTO videos (section, topic, message_id, telegram_link, published_week)
                VALUES (?, ?, ?, ?, ?)
                """,
                (section, topic, message_id, telegram_link, published_week),
            )
            conn.commit()

    def video_list_all(self) -> list:
        """استرجع كل المقاطع."""
        with self.connection() as conn:
            rows = conn.execute("SELECT * FROM videos ORDER BY published_week").fetchall()
            return [dict(row) for row in rows]

    # ===== MEDIA LOG =====
    def log_media(self, user_id: int, media_type: str) -> None:
        """سجّل محاولة إرسال وسائط — بيانات لقرار دعم الصوت لاحقًا."""
        with self.connection() as conn:
            conn.execute(
                "INSERT INTO media_log (user_id, media_type) VALUES (?, ?)",
                (user_id, media_type),
            )
            conn.commit()