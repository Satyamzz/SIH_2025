from fastapi import APIRouter
from demo_data import get_demo_data
from pydantic import BaseModel
router = APIRouter()

class Year(BaseModel):
    year: int


# POST endpoint
@router.post("/filter/graduation_year")
def yearfilter(req:Year):
    data=get_demo_data()
    filtered=[]
    alumni=data.get("alumni",[])
    for person in alumni:
        curr=person.get("id")
        if(req==person.get("graduation_year")):
            filtered.append(curr)
    return {
        "student passed out this year":filtered
    }