# ==========================
# DEEK AI CHAT TOOL
# ==========================

from ai import ask
from response import Response


def chat_tool(request):

    if request.context:

        prompt = f"""
Using the following information:

{request.context}

Answer the user's request:

{request.question}
"""

        answer = ask(prompt)

    else:

        answer = ask(request.question)

    return Response(
        success=True,
        message=answer,
        source="CHAT"
    )
