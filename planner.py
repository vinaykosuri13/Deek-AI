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

        # Natural language calculator
        calculator_keywords = [
            "calculate",
            "what is",
            "compute",
            "evaluate"
        ]

        if any(keyword in question for keyword in calculator_keywords):

            expression = question

            for keyword in calculator_keywords:
                expression = expression.replace(keyword, "")

            expression = expression.replace("?", "").strip()

            if re.fullmatch(r"[0-9+\-*/().% ]+", expression):
                request.question = expression

                return [
                    {"tool": "CALCULATOR"}
                ]

        # Direct mathematical expression
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
