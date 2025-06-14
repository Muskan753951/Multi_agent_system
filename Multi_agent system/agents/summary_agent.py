

def summarize_delay_risk(weather_data: dict) -> str:
    """
    Naively decides if delay is likely based on bad weather.
    """
    conditions = weather_data.get("conditions", "").lower()
    wind = weather_data.get("wind_speed", 0)

    risky_weather = ["storm", "rain", "thunder", "snow"]
    delay_possible = any(word in conditions for word in risky_weather) or wind > 30

    if delay_possible:
        return "There is a high chance the launch may be delayed due to weather."
    else:
        return "Weather conditions look favorable. No delay expected."
