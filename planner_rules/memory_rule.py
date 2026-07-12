# ==========================
# DEEK AI MEMORY RULE
# ==========================

def match(request):

    question = request.question.lower().strip()

    # Retrieve personal information
    if (
        "what's my" in question or
        "what is my" in question or
        "do you remember" in question
    ):
        return [
            {"tool": "MEMORY_SEARCH"},
            {"tool": "CHAT"}
        ]

    # Save personal information
    if (
        "my name is" in question or
        "i am" in question or
        "my favorite" in question or
        "i like" in question
    ):
        return [
            {"tool": "CHAT"},
            {"tool": "MEMORY"}
        ]

    return None
