# ==========================
# DEEK AI PLANNER
# ==========================

class Planner:

    def create_plan(self, request):

        question = request.question.lower()

        if "summarize" in question:
            return ["SEARCH", "CHAT"]

        return [request.intent]
