import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from fastapi import APIRouter
from utility.data_retireve import get_current_alumni_data

router = APIRouter()

@router.get("/analytics/passout")
def get_grad_year():
    data = get_current_alumni_data()
    alumni = data.get("data", [])

    graduation_counts = {}

    for person in alumni:
        year = person.get("profileDetails", {}).get("graduationYear", None)
        if year is not None:
            graduation_counts[year] = graduation_counts.get(year, 0) + 1

    response = [
        {"Batch": year, "count": count}
        for year, count in sorted(graduation_counts.items())
    ]

    return {"batches": response}
