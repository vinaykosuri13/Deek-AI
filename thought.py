# ==========================
# DEEK AI THOUGHT OBJECT
# AIOS Phase 1
# ==========================

class Thought:
    """
    Shared cognitive object used by all AIOS engines.

    The Thought object is created from a Request and is
    gradually enriched by each engine in the cognitive pipeline.

    Pipeline:

    Request
        ↓
    Understanding Engine
        ↓
    Cognitive Engine
        ↓
    Mission Engine
        ↓
    Planning Engine
        ↓
    Execution Engine
    """

    def __init__(self, request):

        # Original Request
        self.request = request

        # Original Question
        self.question = request.question

        # ---------- Understanding ----------

        # Primary understanding of the request
        self.intent = None

        # Important words/entities extracted
        self.entities = []

        # ---------- Reasoning ----------

        self.need_ai = False
        self.need_search = False
        self.need_memory = False
        self.need_weather = False
        self.need_datetime = False
        self.need_calculator = False

        # ---------- Mission ----------

        self.goal = None

        # ---------- Planning ----------

        self.plan = []

        # ---------- Execution ----------

        self.context = ""

        self.tool_results = []

        # ---------- Metadata ----------

        self.confidence = 1.0

    def add_entity(self, entity):

        if entity not in self.entities:
            self.entities.append(entity)

    def add_tool_result(self, tool_name, result):

        self.tool_results.append({
            "tool": tool_name,
            "result": result
        })

    def set_goal(self, goal):

        self.goal = goal

    def add_plan_step(self, tool):

        self.plan.append({
            "tool": tool
        })

    def to_dict(self):

        return {

            "question": self.question,

            "intent": self.intent,

            "entities": self.entities,

            "goal": self.goal,

            "need_ai": self.need_ai,

            "need_search": self.need_search,

            "need_memory": self.need_memory,

            "need_weather": self.need_weather,

            "need_datetime": self.need_datetime,

            "need_calculator": self.need_calculator,

            "plan": self.plan,

            "context": self.context,

            "tool_results": self.tool_results,

            "confidence": self.confidence

        }

    def __repr__(self):

        return f"<Thought goal={self.goal} plan={len(self.plan)} steps>"
