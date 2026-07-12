# ==========================
# DEEK AI INTENT DETECTOR
# ==========================

import re


def detect_intent(question):

    question = question.lower().strip()

    # Calculator
    if re.fullmatch(r"[0-9+\-*/().% ]+", question):
        return "CALCULATOR"

    if any(word in question for word in [
        "calculate",
        "compute",
        "evaluate"
    ]):
        return "CALCULATOR"

    # Date & Time
    if any(word in question for word in [
        "time",
        "date",
        "today",
        "day"
    ]):
        return "DATETIME"

    # Weather
    if any(word in question for word in [
        "weather",
        "temperature",
        "forecast",
        "rain",
        "climate"
    ]):
        return "WEATHER"

    # Search
    if any(word in question for word in [
        "latest",
        "news",
        "search",
        "find",
        "look up"
    ]):
        return "SEARCH"

    # Default
    return "CHAT"
