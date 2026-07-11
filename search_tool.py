# ==========================
# DEEK AI SEARCH TOOL
# ==========================

from search import search_web, format_results
from ai import ask
from response import Response


def search_tool(request):

    results = search_web(request.question)

    context = format_results(results)

    request.context = context

    prompt = f"""
Use these search results to answer the user's question.

Search Results:

{context}

Question:
{request.question}
"""

    answer = ask(prompt)

    return Response(
        success=True,
        message=answer,
        source="SEARCH"
    )
