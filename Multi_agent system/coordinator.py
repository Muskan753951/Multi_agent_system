import sys
import os
import requests

# Add the 'agents' directory
AGENT_DIR = os.path.join(os.path.dirname(__file__), "agents")
sys.path.insert(0, AGENT_DIR)

#  Import from agent files directly 
from planner_agent import plan_steps
from launch_agent import find_next_launch
from weather_agent import get_weather
from summary_agent import summarize_delay_risk as summarize_risk


def get_launchpad_coords(launchpad_id):
    res = requests.get(f"https://api.spacexdata.com/v4/launchpads/{launchpad_id}")
    if res.status_code == 200:
        data = res.json()
        return data["latitude"], data["longitude"]
    return None, None

def run_pipeline(user_goal):
    steps = plan_steps(user_goal)
    data = {}

    for step in steps:
        if step == "find_next_launch":
            launch_info = find_next_launch()
            data["launch"] = launch_info
            lat, lon = get_launchpad_coords(launch_info["launchpad"])
            data["coords"] = {"lat": lat, "lon": lon}

        elif step == "check_weather":
            coords = data.get("coords", {})
            if coords:
                weather_info = get_weather(coords["lat"], coords["lon"])
                data["weather"] = weather_info

        elif step == "summarize_risk":
            summary = summarize_risk(data.get("weather", {}))
            data["summary"] = summary

    return data
