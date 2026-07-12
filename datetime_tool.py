# ==========================
# DEEK AI DATE & TIME TOOL
# ==========================

from datetime import datetime
from response import Response


def datetime_tool(request):

    question = request.question.lower()

    if "time" in question:

        current_time = datetime.now().strftime("%I:%M:%S %p")

        return Response(
            success=True,
            message=current_time,
            source="DATETIME"
        )

    current_date = datetime.now().strftime("%d %B %Y")

    return Response(
        success=True,
        message=current_date,
        source="DATETIME"
    )
