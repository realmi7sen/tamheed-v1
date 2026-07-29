"""
مولّد أكواد الاشتراك لتمهيد.

يشغّل مرة وحدة (أو كل ما تحتاج دفعة جديدة):
    python gencodes.py 75
    python gencodes.py 75 --prefix TAMHEED --out codes.txt

يطبع الأكواد ويخزّنها في نفس قاعدة بيانات البوت.
كل كود يُستخدم مرة وحدة فقط (single-use)، والتحقق يتم في db.redeem_code.
"""

import argparse
import os
import secrets
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).resolve().parent

try:
    from dotenv import load_dotenv
    load_dotenv(PROJECT_DIR / ".env")
except Exception:
    pass

from database.db import TamheedDB


def make_code(prefix: str) -> str:
    token = secrets.token_hex(3).upper()
    return f"{prefix}-{token}"


def main() -> None:
    parser = argparse.ArgumentParser(description="توليد أكواد اشتراك تمهيد")
    parser.add_argument("count", type=int, help="عدد الأكواد")
    parser.add_argument("--prefix", default="TAMHEED", help="بادئة الكود")
    parser.add_argument("--out", default=None, help="ملف نصي لحفظ الأكواد (اختياري)")
    args = parser.parse_args()

    if args.count <= 0:
        print("العدد لازم يكون أكبر من صفر.")
        sys.exit(1)

    db_path = os.environ.get("DB_PATH", "tamheed.db")
    db = TamheedDB(db_path)

    codes = []
    seen = set()
    while len(codes) < args.count:
        code = make_code(args.prefix)
        if code in seen:
            continue
        seen.add(code)
        codes.append(code)

    for code in codes:
        db.code_add(code)

    print(f"تم توليد وتخزين {len(codes)} كود في: {db_path}\n")
    for code in codes:
        print(code)

    if args.out:
        out_path = Path(args.out)
        out_path.write_text("\n".join(codes) + "\n", encoding="utf-8")
        print(f"\nحُفظت أيضاً في: {out_path.resolve()}")


if __name__ == "__main__":
    main()