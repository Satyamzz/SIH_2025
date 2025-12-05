import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from fastapi import APIRouter
from demo_data.alumni_data import get_demo_data

router = APIRouter()

@router.get("/analytics/skills")
def skillfilter():
    data=get_demo_data()
    skill_count={}
    alumni=data.get("alumni",[])
    for person in alumni:
        for sk in person["skills"]:
            if(sk not in skill_count):
                skill_count[sk]=1
            else:
                skill_count[sk]+=1
    response = [
        {"skill":skill, "count": count}
        for skill, count in skill_count.items()
    ]
    return {"Skills": response}

