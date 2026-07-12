# ==========================
# DEEK AI PLANNER
# ==========================

from planner_rules.calculator_rule import match as calculator_rule


class Planner:

    def create_plan(self, request):

        question = request.question.lower()

        # Memory retrieval
        if (
            "what's my" in question or
            "what is my" in question or
            "do you remember" in question
        ):
            return [
                {"tool": "MEMORY_SEARCH"},
                {"tool": "CHAT"}
            ]

        # Memory save
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

        # Calculator Rule
        plan = calculator_rule(request)

        if plan:
            return plan

        # Search then summarize
        if "summarize" in question:
            return [
                {"tool": "SEARCH"},
                {"tool": "CHAT"}
            ]

        return [
            {"tool": request.intent}
        ]
