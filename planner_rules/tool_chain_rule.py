# ==========================
# DEEK AI TOOL CHAIN RULE
# ==========================

def match(request):

    question = request.question.lower()

    plan = []

    # Search + Chat
    if "summarize" in question:

        plan.append({"tool": "SEARCH"})
        plan.append({"tool": "CHAT"})

        return plan

    # Memory + Weather
    if "remember" in question and "weather" in question:

        plan.append({"tool": "MEMORY"})
        plan.append({"tool": "WEATHER"})
        plan.append({"tool": "CHAT"})

        return plan

    return None
