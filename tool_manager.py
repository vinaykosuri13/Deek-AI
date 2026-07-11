# ==========================
# DEEK AI TOOL MANAGER
# ==========================

from search_tool import search_tool
from chat_tool import chat_tool


def execute_tool(intent, question):

    print(f"Selected Tool: {intent}")

    if intent == "SEARCH":
        return search_tool(question)

    elif intent == "CHAT":
        return chat_tool(question)

    else:
        return "Tool not implemented."
