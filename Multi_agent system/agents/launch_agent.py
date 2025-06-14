
import requests

def find_next_launch():
    url = "https://api.spacexdata.com/v4/launches/next"
    res = requests.get(url)
    data = res.json()

    return {
        "mission": data.get("name"),
        "launchpad": data.get("launchpad"),
        "date_utc": data.get("date_utc")
    }
