# ==========================
# DEEK AI WEATHER TOOL
# ==========================

from response import Response
from weather_service import get_weather

WEATHER_CODES = {
    0: "Clear Sky",
    1: "Mainly Clear",
    2: "Partly Cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing Rime Fog",
    51: "Light Drizzle",
    53: "Moderate Drizzle",
    55: "Dense Drizzle",
    61: "Light Rain",
    63: "Moderate Rain",
    65: "Heavy Rain",
    71: "Light Snow",
    73: "Moderate Snow",
    75: "Heavy Snow",
    80: "Rain Showers",
    81: "Heavy Rain Showers",
    82: "Violent Rain Showers",
    95: "Thunderstorm",
    96: "Thunderstorm with Hail",
    99: "Severe Thunderstorm"
}


def weather_tool(request):

    question = request.question.lower()

    city = "Hyderabad"

    if " in " in question:
        city = question.split(" in ", 1)[1]
        city = city.replace("?", "").replace(".", "").strip().title()

    data = get_weather(city)

    if data is None:
        return Response(
            success=False,
            message="City not found.",
            source="WEATHER"
        )

    current = data["current"]

    temperature = current["temperature_2m"]
    weather_code = current["weather_code"]

    condition = WEATHER_CODES.get(weather_code, "Unknown")

    message = (
        f"Current weather in {city}\n"
        f"Temperature: {temperature}°C\n"
        f"Condition: {condition}"
    )

    return Response(
        success=True,
        message=message,
        source="WEATHER"
    )
