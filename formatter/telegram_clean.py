"""تحويل Markdown الخام القادم من النموذج إلى نص نظيف مناسب لتيليجرام.

reply_text العادي في تيليجرام لا يفسّر Markdown، فبدون هذا التنظيف
يشوف الطالب الرموز (## و ** و | جداول) حرفيًا — أول انطباع سيئ.
"""

import re


_HEADER = re.compile(r"^\s{0,3}#{1,6}\s*(.+?)\s*$", re.MULTILINE)
_BOLD = re.compile(r"\*\*(.+?)\*\*")
_ITALIC = re.compile(r"(?<!\*)\*([^*\n]+)\*(?!\*)")
_HR = re.compile(r"^\s*[-—_]{3,}\s*$", re.MULTILINE)
_BULLET = re.compile(r"^\s*[-*]\s+", re.MULTILINE)
_TABLE_SEP = re.compile(r"^\s*\|?[\s:|-]+\|[\s:|-]*$", re.MULTILINE)

# ===== LaTeX =====
_MATH_DELIM = re.compile(r"\$\$?")
_FRAC = re.compile(r"\\frac\s*\{([^{}]+)\}\s*\{([^{}]+)\}")
_SQRT = re.compile(r"\\sqrt\s*\{([^{}]+)\}")
_TEXT = re.compile(r"\\text\s*\{([^{}]+)\}")
_LEFTRIGHT = re.compile(r"\\(left|right)")
_SPACING = re.compile(r"\\[,;:! ]|\\quad|\\qquad")

_LATEX_SYMBOLS = {
    r"\infty": "∞",
    r"\to": "→",
    r"\rightarrow": "→",
    r"\int": "∫",
    r"\sum": "Σ",
    r"\cdot": "·",
    r"\times": "×",
    r"\pm": "±",
    r"\geq": "≥",
    r"\leq": "≤",
    r"\neq": "≠",
    r"\approx": "≈",
    r"\varepsilon": "ε",
    r"\epsilon": "ε",
    r"\alpha": "α",
    r"\beta": "β",
    r"\theta": "θ",
    r"\pi": "π",
    r"\,": " ",
}


def _clean_latex(text: str) -> str:
    text = _FRAC.sub(r"(\1)/(\2)", text)
    text = _SQRT.sub(r"√(\1)", text)
    text = _TEXT.sub(r"\1", text)
    text = _LEFTRIGHT.sub("", text)
    for latex, symbol in _LATEX_SYMBOLS.items():
        text = text.replace(latex, symbol)
    text = _SPACING.sub(" ", text)
    text = _MATH_DELIM.sub("", text)
    return text


def _convert_table_row(line: str) -> str:
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    cells = [c for c in cells if c]
    return " ← ".join(cells)


def clean_markdown(text: str) -> str:
    # LaTeX أولًا: نحوّل \frac و \sqrt والرموز قبل أي شي
    text = _clean_latex(text)

    # جداول: صف الفواصل يُحذف، وكل صف يتحول لسطر «خلية ← خلية»
    text = _TABLE_SEP.sub("", text)
    lines = []
    for line in text.split("\n"):
        if line.count("|") >= 2:
            lines.append(_convert_table_row(line))
        else:
            lines.append(line)
    text = "\n".join(lines)

    # عناوين ## تتحول لسطر بارز بدون رموز
    text = _HEADER.sub(lambda m: f"📌 {m.group(1)}", text)
    # خطوط أفقية تُحذف
    text = _HR.sub("", text)
    # **غامق** و *مائل* تُنزع رموزها
    text = _BOLD.sub(r"\1", text)
    text = _ITALIC.sub(r"\1", text)
    # نقاط القوائم تصير •
    text = _BULLET.sub("• ", text)
    # ضغط الأسطر الفارغة المتراكمة
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()