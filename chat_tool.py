# ==========================
# DEEK AI CHAT TOOL
# ==========================

from ai import ask
from response import Response


def chat_tool(request):

    if request.context:

        prompt = f"""
You are an AI assistant.

Using ONLY the search results below, answer the user's request.

Search Results:
{request.context}

User Request:
{request.question}

If the user asked for a summary, provide a clear summary.
If the user asked a question, answer using only the search results.
"""

        answer = ask(prompt)

    else:

        answer = ask(request.question)

    return Response(
        success=True,
        message=answer,
        source="CHAT"
    )
