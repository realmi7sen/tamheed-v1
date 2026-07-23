"""
لوحة المشرف — أوامر خاصة بك أنت فقط.

/stats     ملخص سريع نصي داخل تيليجرام
/dashboard تقرير HTML كامل يوصلك كملف تفتحه بالمتصفح

الحماية: ADMIN_CHAT_ID في متغيرات البيئة. أي شخص ثاني يرسل الأمر يتجاهله البوت.
"""

import io
import os
import sqlite3
from datetime import datetime

from telegram import Update
from telegram.ext import ContextTypes

ADMIN_CHAT_ID = os.environ.get("ADMIN_CHAT_ID", "")


# ============================================================
# صلاحيات
# ============================================================

def _is_admin(update: Update) -> bool:
    if not ADMIN_CHAT_ID:
        return False
    return str(update.effective_user.id) == str(ADMIN_CHAT_ID)


# ============================================================
# استعلامات
# ============================================================

def _rows(conn, sql, params=()):
    """يرجع list[dict]. لو الجدول غير موجود يرجع قائمة فاضية بدل ما ينهار."""
    try:
        return [dict(r) for r in conn.execute(sql, params).fetchall()]
    except sqlite3.OperationalError:
        return []


def _one(conn, sql, default=0):
    try:
        row = conn.execute(sql).fetchone()
        return row[0] if row and row[0] is not None else default
    except sqlite3.OperationalError:
        return default


def _collect(db_path: str) -> dict:
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row

    data = {
        "students": _one(conn, "SELECT COUNT(*) FROM students"),
        "questions": _one(conn, "SELECT SUM(total_questions) FROM students"),
        "signals": _one(conn, "SELECT COUNT(*) FROM student_signals"),
        "avg_score": _one(conn, "SELECT ROUND(AVG(retrieval_score),3) FROM student_signals"),
        "miss_rate": _one(
            conn,
            "SELECT ROUND(100.0*SUM(CASE WHEN retrieval_score<0.55 THEN 1 ELSE 0 END)/COUNT(*),1) "
            "FROM student_signals",
        ),
        "today": _one(
            conn,
            "SELECT COUNT(*) FROM student_signals WHERE DATE(created_at)=DATE('now')",
        ),
        "returning": _one(
            conn,
            "SELECT COUNT(*) FROM students WHERE DATE(first_seen) != DATE(last_seen)",
        ),
        "bands": _rows(conn, """
            SELECT CASE
                WHEN retrieval_score < 0.55 THEN 'ضعيف — أقل من 0.55'
                WHEN retrieval_score < 0.70 THEN 'متوسط — 0.55 إلى 0.70'
                WHEN retrieval_score < 0.80 THEN 'جيد — 0.70 إلى 0.80'
                ELSE 'ممتاز — فوق 0.80' END AS band,
                COUNT(*) AS n
            FROM student_signals GROUP BY band
        """),
        "topics": _rows(conn, """
            SELECT topic, COUNT(*) n,
                   ROUND(AVG(retrieval_score),3) avg_score,
                   ROUND(MIN(retrieval_score),3) min_score
            FROM student_signals
            WHERE topic IS NOT NULL AND topic != ''
            GROUP BY topic ORDER BY avg_score ASC
        """),
        "modes": _rows(conn, """
            SELECT teaching_mode, COUNT(*) n FROM student_signals
            GROUP BY teaching_mode ORDER BY n DESC
        """),
        "student_list": _rows(conn, """
            SELECT user_id, username, first_name, total_questions, first_seen, last_seen
            FROM students ORDER BY total_questions DESC LIMIT 60
        """),
        "daily": _rows(conn, """
            SELECT DATE(created_at) day, COUNT(*) n
            FROM student_signals GROUP BY day ORDER BY day DESC LIMIT 14
        """),
        "recent": _rows(conn, """
            SELECT user_id, topic, teaching_mode, retrieval_score, was_followup, created_at
            FROM student_signals ORDER BY id DESC LIMIT 50
        """),
        "media": _rows(conn, """
            SELECT media_type, COUNT(*) n FROM media_log
            GROUP BY media_type ORDER BY n DESC
        """),
        "followups": _one(conn, "SELECT COUNT(*) FROM student_signals WHERE was_followup=1"),
    }
    conn.close()
    return data


# ============================================================
# /stats — ملخص نصي
# ============================================================

def _text_summary(d: dict) -> str:
    lines = [
        "📊 *تمهيد — ملخص سريع*",
        "",
        f"الطلاب: {d['students']}",
        f"مجموع الأسئلة: {d['questions']}",
        f"أسئلة اليوم: {d['today']}",
        f"طلاب رجعوا في يوم ثاني: {d['returning']}",
        "",
        f"متوسط درجة الاسترجاع: {d['avg_score']}",
        f"نسبة عدم المطابقة: {d['miss_rate']}%",
        f"أسئلة متابعة مرصودة: {d['followups']}",
    ]

    if d["topics"]:
        lines += ["", "*أضعف المواضيع:*"]
        for t in d["topics"][:5]:
            lines.append(f"  {t['avg_score']} — {t['topic']} ({t['n']} سؤال)")

    if d["modes"]:
        lines += ["", "*أنماط التدريس:*"]
        for m in d["modes"]:
            lines.append(f"  {m['n']} — {m['teaching_mode']}")

    if d["media"]:
        lines += ["", "*محاولات وسائط:*"]
        for m in d["media"]:
            lines.append(f"  {m['n']} — {m['media_type']}")

    lines += ["", "_للتقرير الكامل: /dashboard_"]
    return "\n".join(lines)


# ============================================================
# /dashboard — تقرير HTML
# ============================================================

def _color(score) -> str:
    if score is None:
        return "#8b93a3"
    if score < 0.55:
        return "#e05252"
    if score < 0.70:
        return "#e0a852"
    if score < 0.80:
        return "#7ec96f"
    return "#4f8cff"


def _bar(value, maximum, color="#4f8cff") -> str:
    if not maximum:
        return ""
    pct = max(2, round(100 * value / maximum))
    return f'<div class="bar" style="width:{pct}%;background:{color}"></div>'


def _html(d: dict) -> str:
    now = datetime.now().strftime("%Y-%m-%d %H:%M")
    empty = lambda cols: f'<tr><td colspan="{cols}" class="empty">لا توجد بيانات بعد</td></tr>'

    band_max = max([b["n"] for b in d["bands"]], default=1)
    bands = "".join(
        f'<tr><td>{b["band"]}</td><td class="num">{b["n"]}</td>'
        f'<td class="barcell">{_bar(b["n"], band_max)}</td></tr>'
        for b in d["bands"]
    ) or empty(3)

    topic_max = max([t["n"] for t in d["topics"]], default=1)
    topics = "".join(
        f'<tr><td>{t["topic"]}</td><td class="num">{t["n"]}</td>'
        f'<td class="num" style="color:{_color(t["avg_score"])}">{t["avg_score"]}</td>'
        f'<td class="num" style="color:{_color(t["min_score"])}">{t["min_score"]}</td>'
        f'<td class="barcell">{_bar(t["n"], topic_max)}</td></tr>'
        for t in d["topics"]
    ) or empty(5)

    mode_max = max([m["n"] for m in d["modes"]], default=1)
    modes = "".join(
        f'<tr><td>{m["teaching_mode"]}</td><td class="num">{m["n"]}</td>'
        f'<td class="barcell">{_bar(m["n"], mode_max, "#9b7ec9")}</td></tr>'
        for m in d["modes"]
    ) or empty(3)

    day_max = max([x["n"] for x in d["daily"]], default=1)
    daily = "".join(
        f'<tr><td class="mono">{x["day"]}</td><td class="num">{x["n"]}</td>'
        f'<td class="barcell">{_bar(x["n"], day_max, "#5fc9a0")}</td></tr>'
        for x in d["daily"]
    ) or empty(3)

    students = "".join(
        f'<tr><td>{s["first_name"] or "-"}</td>'
        f'<td class="mono">@{s["username"] or "-"}</td>'
        f'<td class="num">{s["total_questions"]}</td>'
        f'<td class="mono small">{s["first_seen"]}</td>'
        f'<td class="mono small">{s["last_seen"]}</td>'
        f'<td class="num">{"✓" if s["first_seen"][:10] != s["last_seen"][:10] else "—"}</td></tr>'
        for s in d["student_list"]
    ) or empty(6)

    recent = "".join(
        f'<tr><td class="mono small">{r["created_at"]}</td>'
        f'<td class="mono small">u{str(r["user_id"])[-5:]}</td>'
        f'<td>{r["topic"] or "-"}</td>'
        f'<td class="mono small">{r["teaching_mode"]}</td>'
        f'<td class="num" style="color:{_color(r["retrieval_score"])}">{r["retrieval_score"]:.3f}</td>'
        f'<td class="num">{"نعم" if r["was_followup"] else "—"}</td></tr>'
        for r in d["recent"]
    ) or empty(6)

    media = "".join(
        f'<tr><td>{m["media_type"]}</td><td class="num">{m["n"]}</td></tr>'
        for m in d["media"]
    ) or empty(2)

    return f"""<!DOCTYPE html>
<html lang="ar" dir="rtl"><head>
<meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>تمهيد — لوحة البيانات</title>
<style>
:root{{--bg:#0f1115;--panel:#171a21;--border:#262b36;--text:#e6e9ef;--muted:#8b93a3}}
*{{box-sizing:border-box}}
body{{margin:0;padding:24px;background:var(--bg);color:var(--text);
font-family:-apple-system,"Segoe UI",Tahoma,sans-serif;font-size:14px;line-height:1.65}}
h1{{font-size:21px;margin:0 0 4px}}
.sub{{color:var(--muted);font-size:12px;margin-bottom:24px}}
.cards{{display:grid;gap:10px;margin-bottom:24px;
grid-template-columns:repeat(auto-fit,minmax(140px,1fr))}}
.card{{background:var(--panel);border:1px solid var(--border);border-radius:10px;padding:14px 16px}}
.card .label{{color:var(--muted);font-size:11px;margin-bottom:5px}}
.card .value{{font-size:24px;font-weight:600}}
section{{background:var(--panel);border:1px solid var(--border);
border-radius:10px;padding:16px 18px;margin-bottom:16px}}
section h2{{font-size:14px;margin:0 0 12px;font-weight:600;
border-bottom:1px solid var(--border);padding-bottom:9px}}
table{{width:100%;border-collapse:collapse}}
th{{text-align:right;color:var(--muted);font-weight:500;font-size:11px;
padding:6px 9px;border-bottom:1px solid var(--border)}}
td{{padding:7px 9px;border-bottom:1px solid rgba(38,43,54,.5)}}
tr:last-child td{{border-bottom:none}}
.num{{text-align:left;font-variant-numeric:tabular-nums;width:66px}}
.mono{{font-family:ui-monospace,Consolas,monospace}}
.small{{font-size:11px;color:var(--muted)}}
.barcell{{width:42%}}
.bar{{height:7px;border-radius:4px}}
.empty{{color:var(--muted);text-align:center;padding:18px}}
.note{{color:var(--muted);font-size:11px;margin-top:9px;
padding-top:9px;border-top:1px solid var(--border)}}
</style></head><body>

<h1>تمهيد — لوحة البيانات</h1>
<div class="sub">{now}</div>

<div class="cards">
<div class="card"><div class="label">الطلاب</div><div class="value">{d['students']}</div></div>
<div class="card"><div class="label">مجموع الأسئلة</div><div class="value">{d['questions']}</div></div>
<div class="card"><div class="label">أسئلة اليوم</div><div class="value">{d['today']}</div></div>
<div class="card"><div class="label">طلاب رجعوا</div><div class="value">{d['returning']}</div></div>
<div class="card"><div class="label">متوسط الاسترجاع</div>
<div class="value" style="color:{_color(d['avg_score'])}">{d['avg_score']}</div></div>
<div class="card"><div class="label">نسبة عدم المطابقة</div><div class="value">{d['miss_rate']}%</div></div>
</div>

<section><h2>توزيع درجات الاسترجاع</h2>
<table><tr><th>النطاق</th><th class="num">العدد</th><th></th></tr>{bands}</table>
<div class="note">تحت 0.55 يعني البوت ما لقى ملف مطابق وجاوب من معرفته العامة.</div></section>

<section><h2>المواضيع — من الأضعف</h2>
<table><tr><th>الموضوع</th><th class="num">الأسئلة</th><th class="num">المتوسط</th>
<th class="num">الأدنى</th><th></th></tr>{topics}</table>
<div class="note">متوسط منخفض + عدد أسئلة مرتفع = فجوة حقيقية في قاعدة المعرفة.</div></section>

<section><h2>النشاط اليومي</h2>
<table><tr><th>اليوم</th><th class="num">الأسئلة</th><th></th></tr>{daily}</table></section>

<section><h2>الطلاب</h2>
<table><tr><th>الاسم</th><th>المعرّف</th><th class="num">الأسئلة</th>
<th>أول ظهور</th><th>آخر ظهور</th><th class="num">رجع؟</th></tr>{students}</table>
<div class="note">عمود «رجع؟» هو مؤشر البقاء الحقيقي — طالب سأل في أكثر من يوم.</div></section>

<section><h2>أنماط التدريس</h2>
<table><tr><th>النمط</th><th class="num">العدد</th><th></th></tr>{modes}</table>
<div class="note">لو نمط واحد يهيمن بالكامل، فـ TeachingModeSelector ما يشتغل فعليًا.</div></section>

<section><h2>محاولات إرسال وسائط</h2>
<table><tr><th>النوع</th><th class="num">العدد</th></tr>{media}</table>
<div class="note">ارتفاع الصوتيات = دليل أن الطلاب يبغون دعم الصوت.</div></section>

<section><h2>آخر 50 إشارة</h2>
<table><tr><th>الوقت</th><th>الطالب</th><th>الموضوع</th><th>النمط</th>
<th class="num">الدرجة</th><th class="num">متابعة</th></tr>{recent}</table></section>

</body></html>"""


# ============================================================
# الأوامر
# ============================================================

class AdminHandler:
    """أوامر المشرف. تُبنى بمسار قاعدة البيانات نفسه الذي يستخدمه البوت."""

    def __init__(self, db_path: str):
        self.db_path = db_path

    async def stats(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not _is_admin(update):
            return
        try:
            data = _collect(self.db_path)
            await update.message.reply_text(_text_summary(data), parse_mode="Markdown")
        except Exception as error:
            await update.message.reply_text(f"خطأ في قراءة البيانات:\n{error}")

    async def dashboard(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        if not _is_admin(update):
            return
        try:
            data = _collect(self.db_path)
            buffer = io.BytesIO(_html(data).encode("utf-8"))
            buffer.name = f"tamheed_{datetime.now():%Y%m%d_%H%M}.html"
            await update.message.reply_document(
                document=buffer,
                filename=buffer.name,
                caption="حمّل الملف وافتحه بالمتصفح 📊",
            )
        except Exception as error:
            await update.message.reply_text(f"خطأ في توليد التقرير:\n{error}")

    async def backup(self, update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        """نسخة كاملة من قاعدة البيانات — للاحتفاظ بها محليًا."""
        if not _is_admin(update):
            return
        try:
            with open(self.db_path, "rb") as f:
                buffer = io.BytesIO(f.read())
            buffer.name = f"tamheed_{datetime.now():%Y%m%d_%H%M}.db"
            await update.message.reply_document(
                document=buffer,
                filename=buffer.name,
                caption="نسخة احتياطية كاملة 💾",
            )
        except Exception as error:
            await update.message.reply_text(f"خطأ في النسخ الاحتياطي:\n{error}")
