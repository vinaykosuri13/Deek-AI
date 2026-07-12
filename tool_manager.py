# ==========================
# DEEK AI TOOL MANAGER
# ==========================

from plugin_loader import load_tools
from response import Response

TOOLS = load_tools()


def execute_plan(plan, request):

    last_response = None

    for step in plan:

        tool_name = step["tool"]

        print(f"Selected Tool: {tool_name}")

        tool = TOOLS.get(tool_name)

        if tool is None:

            return Response(
                success=False,
                message=f"Tool '{tool_name}' not implemented.",
                source="TOOL_MANAGER"
            )

        last_response = tool(request)

        if last_response.message:
            request.context = last_response.message

    return last_response
