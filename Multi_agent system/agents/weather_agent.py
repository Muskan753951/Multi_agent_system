

import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_weather(lat: float, lon: float) -> dict:
    url = (
        f"https://api.openweathermap.org/data/2.5/weather"
        f"?lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    )
    res = requests.get(url)
    if res.status_code != 200:
        return {"error": "Failed to fetch weather"}
    
    data = res.json()
    return {
        "temp": data["main"]["temp"],
        "conditions": data["weather"][0]["description"],
        "wind_speed": data["wind"]["speed"]
    }
