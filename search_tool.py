# ==========================
# DEEK AI SEARCH TOOL
# ==========================

from search import search_web, format_results
from response import Response


def search_tool(request):

    results = search_web(request.question)

    context = format_results(results)

    # Save raw search results for the next tool
    request.context = context

    return Response(
        success=True,
        message=context,
        source="SEARCH"
    )
