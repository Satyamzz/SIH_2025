import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import APIRouter, HTTPException, Query
import numpy
from demo_data.alumni_data import get_demo_data as aa
from demo_data.student_data import get_demo_data as sa

alum=aa()
stud=sa()

router = APIRouter()
@router.post("/recommend/skill")
def recommend_mentors(stu,alu):
    alumni=alum.get("alumni")
    def skill_match_score(student_skills, alumni_skills):
        student_set = set(student_skills)
        alumni_set = set(alumni_skills)

        matches = student_set.intersection(alumni_set)
        score = len(matches) / max(len(alumni_set), 1)
        return score, list(matches)
    
    recommendations = []
    for alu in alumni:
        score, overlap = skill_match_score(stu["skills"], alu["skills"])
        recommendations.append({
            "alumni_name": alu["name"],
            "score": round(score, 2),
            "skill_overlap": overlap
        })

    recommendations.sort(key=lambda x: x["score"], reverse=True)
    for rec in recommendations[:3]:
        if(rec['score']>0):
            print(f"Mentor: {rec['alumni_name']}")
            print(f"Skill Match Score: {rec['score']}")
            print(f"Overlapping Skills: {rec['skill_overlap']}")
            print("-" * 40)
