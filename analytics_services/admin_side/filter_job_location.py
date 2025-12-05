import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from fastapi import APIRouter
from demo_data.alumni_data import get_demo_data
from pydantic import BaseModel
import re
router = APIRouter()

class Loc(BaseModel):
    location: str

@router.post("/filter/location")
def location_filter(req:Loc):
    data=get_demo_data()
    filtered=[]
    alumni=data.get("alumni",[])
    pattern = fr"(?i){re.escape(req.location)}"
    for person in alumni:
        loc = person.get("location", "")
        if re.search(pattern, loc):
            filtered.append(person["id"])
    return {
        "id_on_location":filtered
    }