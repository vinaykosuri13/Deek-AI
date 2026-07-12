# ==========================
# DEEK AI INTENT DETECTOR
# ==========================

import re


def detect_intent(question):

    question = question.lower().strip()

    # Calculator
    if re.fullmatch(r"[0-9+\-*/().% ]+", question):
        return "CALCULATOR"

    calculator_keywords = [
        "calculate",
        "compute",
        "evaluate"
    ]

    if any(word in question for word in calculator_keywords):
        return "CALCULATOR"

    # Date & Time
    datetime_keywords = [
        "time",
        "date",
        "today",
        "day"
    ]

    if any(word in question for word in datetime_keywords):
        return "DATETIME"

    # Search
    search_keywords = [
        "latest",
        "news",
        "search",
        "find",
        "look up"
    ]

    if any(word in question for word in search_keywords):
        return "SEARCH"

    # Default
    return "CHAT"
