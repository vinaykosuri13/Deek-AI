# ==========================
# DEEK AI WEATHER RULE
# ==========================

def match(request):

    question = request.question.lower()

    keywords = [
        "weather",
        "temperature",
        "forecast",
        "rain",
        "climate"
    ]

    if any(keyword in question for keyword in keywords):
        return [
            {"tool": "WEATHER"}
        ]

    return None
