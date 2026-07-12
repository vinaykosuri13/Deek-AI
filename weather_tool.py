# ==========================
# DEEK AI WEATHER TOOL
# ==========================

from response import Response


def weather_tool(request):

    question = request.question.lower()

    city = "Unknown"

    if " in " in question:
        city = question.split(" in ", 1)[1]
        city = city.replace("?", "").replace(".", "").strip().title()

    return Response(
        success=True,
        message=f"Weather service is ready. Requested city: {city}",
        source="WEATHER"
    )
