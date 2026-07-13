# ==========================
# DEEK AI RESPONSE ENGINE
# AIOS Phase 1
# ==========================

from response import Response


class ResponseEngine:
    """
    Final engine in the AIOS pipeline.

    Responsibilities:
    - Convert the internal Thought object
      into a user-facing Response.
    - Select the final message.
    - Keep internal reasoning hidden.
    """

    def process(self, thought):

        # -----------------------------
        # No execution results
        # -----------------------------

        if not thought.tool_results:

            return Response(
                success=False,
                message="I couldn't complete your request.",
                source="RESPONSE_ENGINE"
            )

        # -----------------------------
        # Final Tool Result
        # -----------------------------

        final_result = thought.tool_results[-1]

        tool_name = final_result["tool"]
        message = final_result["result"]

        # -----------------------------
        # Build Metadata
        # -----------------------------

        metadata = {

            "goal": thought.goal,

            "confidence": thought.confidence,

            "tools_used": [

                step["tool"]

                for step in thought.plan

            ]

        }

        # -----------------------------
        # Return Standard Response
        # -----------------------------

        return Response(

            success=True,

            message=message,

            source=tool_name,

            data=thought.to_dict(),

            results=thought.tool_results,

            metadata=metadata

        )
