# ==========================
# DEEK AI SEARCH RULE
# ==========================

def match(request):

    question = request.question.lower().strip()

    if "summarize" in question:

        return [
            {"tool": "SEARCH"},
            {"tool": "CHAT"}
        ]

    return None
