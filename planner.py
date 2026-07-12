# ==========================
# DEEK AI PLANNER
# ==========================

from planner_rules.memory_rule import match as memory_rule
from planner_rules.calculator_rule import match as calculator_rule

RULES = [
    memory_rule,
    calculator_rule,
]


class Planner:

    def create_plan(self, request):

        for rule in RULES:

            plan = rule(request)

            if plan:
                return plan

        question = request.question.lower()

        # Search then summarize
        if "summarize" in question:
            return [
                {"tool": "SEARCH"},
                {"tool": "CHAT"}
            ]

        return [
            {"tool": request.intent}
        ]
