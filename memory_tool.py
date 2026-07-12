# ==========================
# DEEK AI MEMORY TOOL
# ==========================

from memory import add_message
from response import Response


def memory_tool(request):

    add_message("user", request.question)

    return Response(
        success=True,
        message="Memory updated successfully.",
        source="MEMORY"
    )
