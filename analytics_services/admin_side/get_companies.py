import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from fastapi import APIRouter
from utility.data_retireve import get_current_alumni_data
router = APIRouter()

@router.get("/analytics/company")
def get_company_distribution():
    data=get_current_alumni_data()
    alumni = data.get("data", [])
    company_counts = {}
    for person in alumni:
        if not person: continue
        company = person.get("company", "Unknown")
        company_counts[company] = company_counts.get(company, 0) + 1

    response = [
        {"company": company, "count": count}
        for company, count in company_counts.items()
    ]
    return {"companies": response}
    
