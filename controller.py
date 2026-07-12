# ==========================
# DEEK AI CONTROLLER
# ==========================

from memory import add_message
from intent import detect_intent
from request import Request
from planner import Planner
from tool_manager import execute_plan


def process_request(question):

    # Save user message
    add_message("user", question)

    # Detect intent
    intent = detect_intent(question)

    # Create Request object
    request = Request(intent, question)

    print(f"Intent: {request.intent}")

    # Create execution plan
    plan = Planner().create_plan(request)

    print(f"Plan: {plan}")

    # Execute complete plan
    response = execute_plan(plan, request)

    # Save AI response
    add_message("assistant", response.message)

    return response.message
