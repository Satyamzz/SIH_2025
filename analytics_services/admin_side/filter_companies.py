import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from fastapi import APIRouter
from demo_data.alumni_data import get_demo_data
from pydantic import BaseModel
router = APIRouter()

class Company(BaseModel):
    company: str
# POST endpoint
@router.post("/filter/company")
def companyfilter(req:Company):
    data=get_demo_data()
    filtered=[]
    alumni=data.get("alumni",[])
    for person in alumni:
        curr=person.get("id")
        if(req.company.lower()==person.get("company").lower()):
            filtered.append(curr)
    return {
        "alumni working in this company":filtered
    }