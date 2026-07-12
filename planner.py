# ==========================
# DEEK AI PLANNER
# ==========================

class Planner:

    def create_plan(self, request):

        question = request.question.lower()

        # Retrieve personal information (check FIRST)
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

        # Search then summarize
        if "summarize" in question:
            return [
                {"tool": "SEARCH"},
                {"tool": "CHAT"}
            ]

        return [
            {"tool": request.intent}
        ]
