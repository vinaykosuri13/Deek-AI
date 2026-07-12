# ==========================
# DEEK AI CALCULATOR TOOL
# ==========================

from response import Response


def calculator_tool(request):

    expression = request.question.strip()

    try:
        allowed = "0123456789+-*/().% "

        if not all(c in allowed for c in expression):
            raise ValueError("Invalid characters.")

        result = eval(expression, {"__builtins__": {}}, {})

        return Response(
            success=True,
            message=str(result),
            source="CALCULATOR"
        )

    except Exception:

        return Response(
            success=False,
            message="Invalid mathematical expression.",
            source="CALCULATOR"
        )
