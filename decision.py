# ==========================
# DEEK AI DECISION ENGINE
# ==========================

CURRENT_KEYWORDS = [
    "today",
    "latest",
    "news",
    "current",
    "price",
    "weather",
    "stock",
    "live",
    "score",
    "2026"
]

def needs_web_search(question):
    """
    Decide whether the question needs live internet data.
    """

    question = question.lower()

    for word in CURRENT_KEYWORDS:
        if word in question:
            return True

    return False
