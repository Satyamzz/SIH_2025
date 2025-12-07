import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from fastapi import APIRouter
from utility.data_retireve import get_current_alumni_data
from pydantic import BaseModel

router = APIRouter()

class Company(BaseModel):
    company: str
@router.post("/filter/company")
def companyfilter(req:Company):
    data=get_current_alumni_data()
    filtered=[]
    alumni=data.get("data",[])
    for person in alumni:
        curr=person.get("_id")
        if(req.company.lower()==person.get("profileDetails", {}).get("currentCompany", "").lower()):
            filtered.append(curr)
    return {
        "alumni working in this company":filtered
    }