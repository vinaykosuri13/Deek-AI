# ==========================
# DEEK AI PLANNER
# ==========================

from rule_loader import load_rules

RULES = load_rules()


class Planner:

    def create_plan(self, request):

        for rule in RULES:

            plan = rule(request)

            if plan:
                return plan

        return [
            {"tool": request.intent}
        ]
