# ==========================
# DEEK AI WEATHER SERVICE
# ==========================

import requests


def get_coordinates(city):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    response = requests.get(url, params={
        "name": city,
        "count": 1
    })

    data = response.json()

    if "results" not in data:
        return None

    result = data["results"][0]

    return result["latitude"], result["longitude"]


def get_weather(city):

    location = get_coordinates(city)

    if location is None:
        return None

    latitude, longitude = location

    url = "https://api.open-meteo.com/v1/forecast"

    response = requests.get(url, params={
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code"
    })

    return response.json()
    response = requests.get(url, params={
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,weather_code"
    })

    return response.json()
