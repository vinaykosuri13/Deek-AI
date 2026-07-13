# ==========================
# DEEK AI COGNITIVE ENGINE
# AIOS Phase 1
# ==========================

from decision import needs_web_search


class CognitiveEngine:
    """
    Second engine in the AIOS cognitive pipeline.

    Responsibilities:
    - Decide what capabilities are required.
    - Decide whether AI reasoning is needed.
    - Decide whether internet access is needed.
    - Decide whether memory should be used.
    """

    def process(self, thought):

        question = thought.question.lower()

        # ----------------------------------
        # Internet Decision
        # ----------------------------------

        if needs_web_search(question):
            thought.need_search = True

        # ----------------------------------
        # Memory Decision
        # ----------------------------------

        memory_keywords = [

            "remember",
            "memory",
            "recall",
            "previous",
            "earlier",
            "before",
            "last time",
            "my"

        ]

        if any(word in question for word in memory_keywords):

            thought.need_memory = True

        # ----------------------------------
        # AI Reasoning Decision
        # ----------------------------------

        simple_tools = [

            thought.need_calculator,
            thought.need_weather,
            thought.need_datetime

        ]

        if not any(simple_tools):

            thought.need_ai = True

        if thought.need_search:
            thought.need_ai = True

        if thought.need_memory:
            thought.need_ai = True

        # ----------------------------------
        # Confidence Estimation
        # ----------------------------------

        score = 1.0

        if thought.need_search:
            score -= 0.10

        if thought.need_memory:
            score -= 0.05

        if thought.need_ai:
            score -= 0.05

        thought.confidence = max(score, 0.50)

        return thought
