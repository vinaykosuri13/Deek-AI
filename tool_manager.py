# ==========================
# DEEK AI TOOL MANAGER
# ==========================

from search_tool import search_tool
from chat_tool import chat_tool

TOOLS = {
    "SEARCH": search_tool,
    "CHAT": chat_tool,
}


def execute_tool(intent, question):

    print(f"Selected Tool: {intent}")

    tool = TOOLS.get(intent)

    if tool:
        return tool(question)

    return "Tool not implemented."
