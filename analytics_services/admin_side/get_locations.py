import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from fastapi import APIRouter
from demo_data.alumni_data import get_demo_data

router = APIRouter()

@router.get("/analytics/location")
def get_company_distribution():
    data = get_demo_data()          
    alumni = data["alumni"]         
    location_counts = {}
    for person in alumni:
        location = person.get("location", "Unknown")
        location_counts[location] = location_counts.get(location, 0) + 1

    response = [
        {"Location": location, "count": count}
        for location, count in location_counts.items()
    ]
    return {"Location": response}