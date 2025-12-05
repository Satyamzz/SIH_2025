import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from fastapi import  APIRouter
from collections import Counter
from demo_data.alumni_data import  get_demo_data
router=APIRouter()


#may have to change a bit when adding mongo db collecation
@router.get("/analytics/summary")
def alumni_analytics():
    alumni_data = get_demo_data()       # returns dict
    data = alumni_data["alumni"]        # list of alumni dicts

    total = len(data)
    year_count = Counter(a.get("graduation_year") for a in data)
    branch_count = Counter(a.get("branch") for a in data)
    company_count = Counter(a.get("company") for a in data).most_common(10)

    all_skills = []
    for a in data:
        skills = a.get("skills", [])
        if skills:
            all_skills.extend(skills)

    skill_count = Counter(all_skills).most_common(15)

    return {
        "total_alumni": total,
        "by_year": dict(year_count),
        "by_branch": dict(branch_count),
        "top_companies": [{"company": c, "count": n} for c, n in company_count],
        "top_skills": [{"skill": s, "count": n} for s, n in skill_count]
    }
