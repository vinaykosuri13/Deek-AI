# ==========================
# DEEK AI CONTROLLER
# ==========================

from memory import add_message
from intent import detect_intent
from tool_manager import execute_tool
from request import Request


def process_request(question):

    # Save user message
    add_message("user", question)

    # Detect intent
    intent = detect_intent(question)

    # Create Request object
    request = Request(intent, question)

    print(f"Intent: {request.intent}")

    # Execute tool
    response = execute_tool(request)

    # Save AI response
    add_message("assistant", response.message)

    return response.message
