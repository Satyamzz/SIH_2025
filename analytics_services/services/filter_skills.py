import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from fastapi import APIRouter
from demo_data.alumni_data import get_demo_data
from pydantic import BaseModel
router = APIRouter()

class Skill(BaseModel):
    skill: str


# POST endpoint
@router.post("/filter/skills")
def skillfilter(req:Skill):
    data=get_demo_data()
    filtered=[]
    alumni=data.get("alumni",[])
    for person in alumni:
        curr=person.get("id")
        for sk in person["skills"]:
            if(req.skill.lower()==sk.lower() and curr not in filtered):
                filtered.append(curr)
                break
    return {
        "alumni_with_skill": filtered,
        "count": len(filtered)
    }