import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from fastapi import APIRouter
from utility.data_retireve import get_current_alumni_data
router = APIRouter()

@router.get("/analytics/branch")
def get_branch_distribution():
    data=get_current_alumni_data()
    alumni = data.get("data", [])
    branch_counts = {}
    for person in alumni:
        if not person: continue # Skip None records
        branch = person.get("branch", "Unknown")
        branch_counts[branch] = branch_counts.get(branch, 0) + 1

    response = [
        { "branch":branch, "count": count}
        for branch, count in branch_counts.items()
    ]
    return {"branch": response}
    
