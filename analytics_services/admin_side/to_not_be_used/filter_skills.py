import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from fastapi import APIRouter
from utility.data_retireve import get_current_alumni_data
from pydantic import BaseModel

router = APIRouter()

class Skill(BaseModel):
    skill: str


# POST endpoint
@router.post("/filter/skills")
def skillfilter(req:Skill):
    data=get_current_alumni_data()
    filtered=[]
    alumni=data.get("data",[])
    for person in alumni:
        curr=person.get("_id")
        for sk in person.get("profileDetails", {}).get("skills", []):
            if(req.skill.lower()==sk.lower() and curr not in filtered):
                filtered.append(curr)
                break
    return {
        "alumni_with_skill": filtered,
        "count": len(filtered)
    }