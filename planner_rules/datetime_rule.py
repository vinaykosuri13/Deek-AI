# ==========================
# DEEK AI DATETIME RULE
# ==========================

def match(request):

    question = request.question.lower()

    keywords = [
        "time",
        "date",
        "today",
        "day"
    ]

    if any(keyword in question for keyword in keywords):

        return [
            {"tool": "DATETIME"}
        ]

    return None
