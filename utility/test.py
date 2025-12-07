
# from fastapi import APIRouter
from data_retireve import get_current_alumni_data

# router = APIRouter()

# @router.get("/analytics/skills")
def skillfilter():
    data=get_current_alumni_data()
    skill_count={}
    alumni=data.get("data",[])
    for person in alumni:
        for sk in person["profileDetails"]["skills"]:
            if(sk not in skill_count):
                skill_count[sk]=1
            else:
                skill_count[sk]+=1
    response = [
        {"skill":skill, "count": count}
        for skill, count in skill_count.items()
    ]
    return {"Skills": response}

print(skillfilter())