import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from fastapi import APIRouter
from utility.data_retireve import get_current_alumni_data
from pydantic import BaseModel

router = APIRouter()

class Year(BaseModel):
    year: int


# POST endpoint
@router.post("/filter/graduation_year")
def yearfilter(req:Year):
    data=get_current_alumni_data()
    filtered=[]
    alumni=data.get("data",[])
    for person in alumni:
        curr=person.get("_id")
        if(req.year==person.get("profileDetails", {}).get("graduationYear")):
            filtered.append(curr)
    return {
        "student passed out this year":filtered
    }