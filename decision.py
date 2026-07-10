# ==========================
# DEEK AI DECISION ENGINE
# Version: 0.2 Stable
# ==========================

CURRENT_KEYWORDS = [

    # Time
    "today",
    "yesterday",
    "tomorrow",
    "latest",
    "current",
    "now",
    "recent",
    "new",
    "breaking",
    "live",
    "update",
    "updates",

    # News
    "news",
    "headline",
    "headlines",

    # Weather
    "weather",
    "temperature",
    "forecast",
    "rain",
    "humidity",
    "storm",
    "climate",

    # Sports
    "score",
    "scores",
    "match",
    "won",
    "winner",
    "result",
    "results",
    "ipl",
    "cricket",
    "football",
    "soccer",
    "tennis",
    "kabaddi",
    "nba",

    # Finance
    "price",
    "stock",
    "stocks",
    "bitcoin",
    "crypto",
    "gold",
    "silver",
    "market",
    "share",

    # Technology
    "release",
    "released",
    "launch",
    "launched",
    "announcement",
    "ai news",

    # Elections & Government
    "election",
    "vote",
    "government",

    # Years
    "2025",
    "2026",
    "2027",
    "2028"
]

def needs_web_search(question):
    """
    Decide if the question requires live internet information.
    """

    question = question.lower()

    for keyword in CURRENT_KEYWORDS:
        if keyword in question:
            return True

    return False
