# ==========================
# DEEK AI MEMORY SEARCH TOOL
# ==========================

from memory import search_memory
from response import Response


def memory_search_tool(request):

    results = search_memory(request.question)

    if results:

        text = "\n".join(
            item["message"] for item in results
        )

    else:

        text = "No relevant memory found."

    return Response(
        success=True,
        message=text,
        source="MEMORY_SEARCH"
    )
