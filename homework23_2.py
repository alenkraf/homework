import requests
import json
from datetime import datetime

def get_war_stat(date_from: str, date_to: str):
    
    
    try:
        datetime.strptime(date_from, "%Y-%m-%d")
        datetime.strptime(date_to, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use 'year-month-day' format.")
        return

    base_url = "https://russianwarship.rip/api/v2/statistics/"
    
    try:
        from_stats = requests.get(base_url + date_from).json()["data"]["stats"]
        to_stats = requests.get(base_url + date_to).json()["data"]["stats"]
    except requests.RequestException as e:
        print(f"Error in making requests: {e}")
        return

    new_stats = {
        "personnel_units_diff": to_stats["personnel_units"] - from_stats["personnel_units"],
        "tanks_diff": to_stats["tanks"] - from_stats["tanks"],
    }
    
    output_path = "your_stats.json"
    
    with open(output_path, "w") as w_s:
        json.dump(new_stats, w_s)

get_war_stat("2022-03-01", "2023-03-01")
