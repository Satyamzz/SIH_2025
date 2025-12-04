import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from fastapi import APIRouter
from demo_data.alumni_data import get_demo_data

router = APIRouter()

@router.get("/analytics/passout")
def get_grad_year():
    data = get_demo_data()
    alumni = data.get("alumni", [])

    graduation_counts = {}

    for person in alumni:
        year = person.get("graduation_year", None)
        if year is not None:
            graduation_counts[year] = graduation_counts.get(year, 0) + 1

    response = [
        {"Batch": year, "count": count}
        for year, count in sorted(graduation_counts.items())
    ]

    return {"batches": response}
