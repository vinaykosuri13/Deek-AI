# ==========================
# DEEK AI PLANNER
# ==========================

import re


class Planner:

    def create_plan(self, request):

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

        # Calculator
        if re.fullmatch(r"[0-9+\-*/().% ]+", question):
            return [
                {"tool": "CALCULATOR"}
            ]

        # Search then summarize
        if "summarize" in question:
            return [
                {"tool": "SEARCH"},
                {"tool": "CHAT"}
            ]

        return [
            {"tool": request.intent}
        ]
