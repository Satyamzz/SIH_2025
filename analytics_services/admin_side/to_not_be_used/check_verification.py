import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

from fastapi import APIRouter, HTTPException
from utility.data_retireve import get_current_alumni_data
from pydantic import BaseModel

router = APIRouter()

class Id(BaseModel):
    id: int

@router.post("/alumni/check_verified")
def check_verified(req: Id):
    data = get_current_alumni_data()
    alumni = data.get("data", [])
    for person in alumni:
        if person.get("_id") == req.id:
            is_verified = person.get("profileDetails",{}).get("verified", False)

            return {
                "alumni_id": req.id,
                "name": person.get("name"),
                "verified": is_verified,
                "completion_percent": person.get("profileDetails", {}).get("profileCompletion"),
                "message": "This alumni is verified." if is_verified else "This alumni is NOT verified."
            }
    return {
        "error": f"No alumni found with id {req.id}"
    }
