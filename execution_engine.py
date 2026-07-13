# ==========================
# DEEK AI EXECUTION ENGINE
# AIOS Phase 1
# ==========================

from plugin_loader import load_tools


class ExecutionEngine:
    """
    Executes every step in the execution plan.

    Input:
        Thought

    Output:
        Updated Thought
    """

    def __init__(self):

        self.tools = load_tools()

    def process(self, thought):

        # Clear previous execution context
        thought.context = ""
        thought.tool_results = []

        for step in thought.plan:

            tool_name = step["tool"]

            tool = self.tools.get(tool_name)

            if tool is None:

                thought.add_tool_result(
                    tool_name,
                    "Tool not found."
                )

                continue

            # Execute tool
            response = tool(thought.request)

            # Store execution result
            thought.add_tool_result(
                tool_name,
                response.message
            )

            # Update context for next tool
            if response.message:

                thought.context = response.message

                # Keep Request synchronized
                thought.request.context = response.message

        return thought
