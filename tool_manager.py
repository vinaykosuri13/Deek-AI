# ==========================
# DEEK AI TOOL MANAGER
# ==========================

from search_tool import search_tool
from chat_tool import chat_tool
from response import Response

TOOLS = {
    "SEARCH": search_tool,
    "CHAT": chat_tool,
}


def execute_tool(request):

    print(f"Selected Tool: {request.intent}")

    tool = TOOLS.get(request.intent)

    if tool:
        return tool(request)

    return Response(
        success=False,
        message="Tool not implemented.",
        source="TOOL_MANAGER"
    )
