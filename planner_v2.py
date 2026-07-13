# ==========================
# DEEK AI PLANNING ENGINE
# AIOS Phase 1
# ==========================


class PlanningEngine:
    """
    AIOS Planning Engine

    Builds an execution plan using the information
    inside the Thought object.
    """

    def process(self, thought):

        # Start with an empty plan
        thought.plan = []

        # -----------------------------
        # Calculator
        # -----------------------------
        if thought.need_calculator:

            thought.add_plan_step("CALCULATOR")

            return thought

        # -----------------------------
        # Date & Time
        # -----------------------------
        if thought.need_datetime:

            thought.add_plan_step("DATETIME")

            return thought

        # -----------------------------
        # Weather
        # -----------------------------
        if thought.need_weather:

            thought.add_plan_step("WEATHER")

            return thought

        # -----------------------------
        # Memory Retrieval
        # -----------------------------
        if thought.need_memory:

            thought.add_plan_step("MEMORY_SEARCH")

        # -----------------------------
        # Internet Search
        # -----------------------------
        if thought.need_search:

            thought.add_plan_step("SEARCH")

        # -----------------------------
        # AI Reasoning
        # -----------------------------
        if thought.need_ai:

            thought.add_plan_step("CHAT")

        # -----------------------------
        # Store Important Information
        # -----------------------------
        remember_words = [

            "remember",
            "save",
            "store",
            "note"

        ]

        if any(word in thought.question.lower() for word in remember_words):

            thought.add_plan_step("MEMORY")

        return thought
