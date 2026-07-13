# ==========================
# DEEK AI UNDERSTANDING ENGINE
# AIOS Phase 1
# ==========================

import re

from thought import Thought


class UnderstandingEngine:
    """
    First engine in the AIOS cognitive pipeline.

    Responsibilities:
    - Create a Thought object.
    - Understand the user's request.
    - Extract basic entities.
    - Detect the primary intent.
    """

    def process(self, request):

        thought = Thought(request)

        question = request.question.lower().strip()

        # -----------------------------
        # Detect Intent
        # -----------------------------

        if re.fullmatch(r"[0-9+\-*/().% ]+", question):

            thought.intent = "CALCULATOR"
            thought.need_calculator = True

        elif any(word in question for word in [
            "calculate",
            "compute",
            "evaluate"
        ]):

            thought.intent = "CALCULATOR"
            thought.need_calculator = True

        elif any(word in question for word in [
            "weather",
            "temperature",
            "forecast",
            "rain",
            "climate"
        ]):

            thought.intent = "WEATHER"
            thought.need_weather = True

        elif any(word in question for word in [
            "time",
            "date",
            "today",
            "day"
        ]):

            thought.intent = "DATETIME"
            thought.need_datetime = True

        elif any(word in question for word in [
            "latest",
            "news",
            "find",
            "search",
            "look up"
        ]):

            thought.intent = "SEARCH"
            thought.need_search = True

        else:

            thought.intent = "CHAT"
            thought.need_ai = True

        # -----------------------------
        # Extract Entities
        # -----------------------------

        words = re.findall(r"\b[a-zA-Z0-9₹]+\b", request.question)

        for word in words:

            if len(word) > 2:

                thought.add_entity(word)

        # -----------------------------
        # Initial Goal
        # -----------------------------

        thought.goal = request.question

        return thought
