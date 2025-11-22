
from fastapi import APIRouter
from demo_data import get_demo_data

router = APIRouter()

@router.get("/analytics/company")
def get_company_distribution():
    data = get_demo_data()          
    alumni = data["alumni"]         
    company_counts = {}
    for person in alumni:
        company = person.get("company", "Unknown")
        company_counts[company] = company_counts.get(company, 0) + 1

    response = [
        {"company": company, "count": count}
        for company, count in company_counts.items()
    ]
    return {"companies": response}
    
