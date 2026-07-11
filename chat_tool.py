# ==========================
# DEEK AI CHAT TOOL
# ==========================

from ai import ask
from response import Response


def chat_tool(question):

    answer = ask(question)

    return Response(
        success=True,
        message=answer
    )
