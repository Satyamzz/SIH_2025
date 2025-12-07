import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))  
from fastapi import APIRouter
from utility.data_retireve import get_current_alumni_data

router = APIRouter()

@router.get("/analytics/skills")
def skillfilter():
    data=get_current_alumni_data()
    skill_count={}
    alumni=data.get("data",[])
    for person in alumni:
        for sk in person.get("profileDetails", {}).get("skills", []):
            if(sk not in skill_count):
                skill_count[sk]=1
            else:
                skill_count[sk]+=1
    response = [
        {"skill":skill, "count": count}
        for skill, count in skill_count.items()
    ]
    return {"Skills": response}

