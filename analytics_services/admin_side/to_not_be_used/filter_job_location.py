import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from fastapi import APIRouter
from utility.data_retireve import get_current_alumni_data
from pydantic import BaseModel
import re

router = APIRouter()

class Loc(BaseModel):
    location: str

@router.post("/filter/location")
def location_filter(req:Loc):
    data=get_current_alumni_data()
    filtered=[]
    alumni=data.get("data",[])
    pattern = fr"(?i){re.escape(req.location)}"
    for person in alumni:
        location_data = person.get("profileDetails", {}).get("location", {})
        if isinstance(location_data, dict):
            loc = f"{location_data.get('city', '')} {location_data.get('state', '')} {location_data.get('country', '')}"
        else:
            loc = str(location_data)
        if re.search(pattern, loc):
            filtered.append(person.get("_id"))
    return {
        "id_on_location":filtered
    }