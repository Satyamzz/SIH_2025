import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))  

from fastapi import APIRouter
from utility.data_retireve import get_current_alumni_data

router = APIRouter()

@router.get("/analytics/location")
def get_company_distribution():
    data = get_current_alumni_data()          
    alumni = data.get("data", [])
    location_counts = {}
    for person in alumni:
        location_data = person.get("profileDetails", {}).get("location", {})
        if isinstance(location_data, dict):
            location = f"{location_data.get('city', '')} {location_data.get('state', '')}" .strip() or "Unknown"
        else:
            location = str(location_data) if location_data else "Unknown"
        location_counts[location] = location_counts.get(location, 0) + 1

    response = [
        {"Location": location, "count": count}
        for location, count in location_counts.items()
    ]
    return {"Location": response}