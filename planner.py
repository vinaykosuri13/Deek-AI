# ==========================
# DEEK AI PLANNER
# ==========================

from planner_rules.tool_chain_rule import match as tool_chain_rule
from planner_rules.memory_rule import match as memory_rule
from planner_rules.calculator_rule import match as calculator_rule
from planner_rules.datetime_rule import match as datetime_rule
from planner_rules.weather_rule import match as weather_rule
from planner_rules.search_rule import match as search_rule

RULES = [
    tool_chain_rule,
    memory_rule,
    calculator_rule,
    datetime_rule,
    weather_rule,
    search_rule,
]


class Planner:

    def create_plan(self, request):

        for rule in RULES:

            plan = rule(request)

            if plan:
                return plan

        return [
            {"tool": request.intent}
        ]
