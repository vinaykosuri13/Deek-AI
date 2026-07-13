# ==========================
# DEEK AI CONTROLLER V2
# AIOS Phase 1
# ==========================

from memory import add_message

from request import Request

from understanding_engine import UnderstandingEngine
from cognitive_engine import CognitiveEngine
from mission_engine import MissionEngine
from planner_v2 import PlanningEngine
from execution_engine import ExecutionEngine
from response_engine import ResponseEngine


class ControllerV2:
    """
    AIOS Controller

    Coordinates the complete AIOS cognitive pipeline.
    """

    def __init__(self):

        self.understanding = UnderstandingEngine()

        self.cognitive = CognitiveEngine()

        self.mission = MissionEngine()

        self.planner = PlanningEngine()

        self.execution = ExecutionEngine()

        self.response_engine = ResponseEngine()

    def process(self, question):

        # -----------------------------
        # Save User Message
        # -----------------------------

        add_message("user", question)

        # -----------------------------
        # Create Request
        # -----------------------------

        request = Request(
            intent=None,
            question=question
        )

        # -----------------------------
        # AIOS Cognitive Pipeline
        # -----------------------------

        thought = self.understanding.process(request)

        thought = self.cognitive.process(thought)

        thought = self.mission.process(thought)

        thought = self.planner.process(thought)

        thought = self.execution.process(thought)

        response = self.response_engine.process(thought)

        # -----------------------------
        # Save Assistant Response
        # -----------------------------

        add_message(
            "assistant",
            response.message
        )

        return response
