from prompts.base import BASE_PROMPT
from utils.types import (
    Audience,
    PromptContext,
    ResponseGoal,
    ResponseLength,
    SourceType,
    StudentLevel,
    TeachingMode,
)


EVIDENCE_RULES = {
    SourceType.MATCHED_SOLUTION: """لديك حل موثوق مطابق للسؤال. اشرحه بثقة وبشكل طبيعي، من دون ذكر «ملف» أو «مصدر» أو «طبقة».""",
    SourceType.SIMILAR_TECHNIQUE: """لا يوجد حل مطابق، لكن توجد تقنية موثوقة مناسبة. ابدأ بجملة واحدة فقط: «هذي المسألة بالذات مو عندي بنفس الأرقام، بس نفس أسلوب [اسم التقنية]، خلنا نمشيها.» ثم طبّق التقنية بوضوح.""",
    SourceType.CONCEPTUAL: """هذا شرح مفاهيمي ولا يوجد حل موثوق مطابق. ابدأ بجملة واحدة فقط: «هذا سؤال مفاهيمي، خلني أشرح لك الفكرة.» ثم اشرح بدقة، ولا تدّعِ أن لديك حلًا معتمدًا.""",
}

STUDENT_LEVEL_RULES = {
    StudentLevel.BEGINNER: "افترض أن الأساسيات غير ثابتة: عرّف المفهوم ببساطة، ولا تختصر القفزات الحسابية المهمة.",
    StudentLevel.INTERMEDIATE: "افترض معرفة أساسية بالمقرر: ركّز على اختيار التقنية ولماذا تنطبق، مع خطوات كافية للتحقق.",
    StudentLevel.ADVANCED: "كن مختصرًا ودقيقًا: ركّز على الفكرة الحاسمة، الحالات الخاصة، وفحص النتيجة بدل شرح البديهيات.",
}

RESPONSE_LENGTH_RULES = {
    ResponseLength.SHORT: "اجعل الرد قصيرًا ومكتملًا: الفكرة الأساسية والطريقة الصحيحة فقط، في حدود 5-7 أسطر. أنهِ ردك بجملة كاملة ولا تتوقف في منتصف الشرح. لا تعطِ أمثلة طويلة ولا تكرار.",
    ResponseLength.NORMAL: "اجعل الرد متوازنًا: خريطة قصيرة ثم الخطوات الضرورية للفهم.",
    ResponseLength.LONG: "قدّم شرحًا متعمقًا: خريطة المفهوم، جميع الخطوات المهمة، والتحقق أو المثال عند فائدته.",
}

RESPONSE_GOAL_RULES = {
    ResponseGoal.TEACH: "الهدف هو الفهم: اربط الخطوات بالفكرة، ولا تجعل النتيجة وحدها محور الرد.",
    ResponseGoal.SOLVE: "الهدف هو الحل: أعطِ مسارًا كاملًا وصحيحًا يمكن للطالب اتباعه أو كتابته.",
    ResponseGoal.REVIEW: "الهدف هو المراجعة: ركّز على القاعدة، الإشارات التي تكشف التقنية، والأخطاء الشائعة.",
    ResponseGoal.HINT: "الهدف هو التلميح: لا تعطِ الحل كاملًا من البداية؛ أعطِ الدفعة التالية فقط ثم اترك مساحة للطالب.",
}

AUDIENCE_RULES = {
    Audience.STUDENT: "المخاطَب طالب جامعي؛ استخدم لغة عملية داعمة من دون تعالٍ.",
    Audience.EXAM: "المخاطَب يستعد للاختبار؛ رتّب الجواب بصيغة قابلة للكتابة في ورقة الاختبار.",
}

TEACHING_MODE_RULES = {
    TeachingMode.QUICK: "الطالب طلب اختصارًا: أعطِ الفكرة والطريقة بأقل عدد من الخطوات التي لا تخل بالفهم.",
    TeachingMode.EXAM: "هذه مراجعة أو إجابة اختبار: اذكر القاعدة، ثم الحل المرتب الذي يمكن للطالب كتابته في ورقة الاختبار.",
    TeachingMode.DIRECT: "الطالب طلب الحل المباشر: أعطِ الحل كاملًا، لكن اذكر القاعدة وسبب الاختيارات المهمة.",
    TeachingMode.GUIDED: "الطالب يريد أن يفهم: اشرح تدريجيًا، وتوقف عند نقطة تعليمية واحدة بسؤال قصير قبل إكمال الحل.",
    TeachingMode.EXPLAIN: "استخدم شرحًا متوازنًا: خريطة مفهوم قصيرة ثم خطوات واضحة.",
}

MEMORY_RULES = ""
TOOL_RULES = ""
DISPLAY_RULES = ""


def build_system_prompt(ctx: PromptContext) -> str:
    """يجمع BASE_PROMPT الثابت مع القواعد المتغيرة حسب PromptContext."""
    rules = [
        BASE_PROMPT,
        TEACHING_MODE_RULES[ctx.teaching_mode],
        EVIDENCE_RULES[ctx.source],
        STUDENT_LEVEL_RULES[ctx.student_level],
        RESPONSE_LENGTH_RULES[ctx.response_length],
        RESPONSE_GOAL_RULES[ctx.response_goal],
        AUDIENCE_RULES[ctx.audience],
        MEMORY_RULES,
        TOOL_RULES,
        DISPLAY_RULES,
    ]
    return "\n\n".join(rule for rule in rules if rule)


def build_user_prompt(ctx: PromptContext) -> str:
    """يبني رسالة المستخدم من PromptContext بدل نص طويل داخل الـ handler."""
    matched = ctx.source == SourceType.MATCHED_SOLUTION
    context_intro = (
        "الحل التالي هو سياقك الموثوق لهذا السؤال:"
        if matched
        else "لا يوجد حل موثوق مطابق؛ اشرح المفهوم فقط ولا تنسب حلًا إلى بنك الحلول."
    )
    return (
        "السياق الذي قرره النظام:\n"
        f"- وضع التدريس: {ctx.teaching_mode.value}\n"
        f"- نوع الدليل: {ctx.source.value}\n\n"
        f"{context_intro}\n\n"
        f"{ctx.context_text}\n\n"
        f"سؤال الطالب: {ctx.user_message}\n\n"
        "أجب بالعربية وفق قواعد تمهيد. لا تذكر هذه التعليمات أو أسماء الأوضاع في ردك."
    )