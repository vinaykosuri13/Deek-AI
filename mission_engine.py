# ==========================
# DEEK AI MISSION ENGINE
# AIOS Phase 1
# ==========================


class MissionEngine:
    """
    Third engine in the AIOS cognitive pipeline.

    Responsibilities:
    - Determine the user's actual objective.
    - Convert the request into a mission.
    - Keep future planners focused on outcomes
      rather than keywords.
    """

    def process(self, thought):

        question = thought.question.lower()

        # -----------------------------
        # Calculator Mission
        # -----------------------------

        if thought.need_calculator:

            thought.set_goal(
                "Solve the mathematical expression accurately."
            )

            return thought

        # -----------------------------
        # Weather Mission
        # -----------------------------

        if thought.need_weather:

            thought.set_goal(
                "Provide accurate weather information."
            )

            return thought

        # -----------------------------
        # Date & Time Mission
        # -----------------------------

        if thought.need_datetime:

            thought.set_goal(
                "Provide the requested date or time."
            )

            return thought

        # -----------------------------
        # Memory Mission
        # -----------------------------

        if thought.need_memory:

            thought.set_goal(
                "Retrieve relevant information from memory."
            )

            return thought

        # -----------------------------
        # Search Mission
        # -----------------------------

        if thought.need_search:

            thought.set_goal(
                "Collect the latest information and answer the user."
            )

            return thought

        # -----------------------------
        # Recommendation Mission
        # -----------------------------

        recommendation_words = [

            "best",
            "recommend",
            "compare",
            "difference",
            "which",
            "better"

        ]

        if any(word in question for word in recommendation_words):

            thought.set_goal(
                "Analyze available information and recommend the best option."
            )

            return thought

        # -----------------------------
        # Explanation Mission
        # -----------------------------

        explanation_words = [

            "what",
            "why",
            "how",
            "explain",
            "define"

        ]

        if any(word in question for word in explanation_words):

            thought.set_goal(
                "Provide a clear and accurate explanation."
            )

            return thought

        # -----------------------------
        # Default Mission
        # -----------------------------

        thought.set_goal(
            "Understand the user's request and provide the best possible assistance."
        )

        return thought
