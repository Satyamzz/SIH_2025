import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from fastapi import APIRouter
from demo_data.alumni_data import get_demo_data

router = APIRouter()

@router.get("/analytics/branch")
def get_branch_distribution():
    data=get_demo_data()
    alumni = data["alumni"]         
    branch_counts = {}
    for person in alumni:
        branch = person.get("branch", "Unknown")
        branch_counts[branch] = branch_counts.get(branch, 0) + 1

    response = [
        { "branch":branch, "count": count}
        for branch, count in branch_counts.items()
    ]
    return {"branch": response}
    
