import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))  

from fastapi import APIRouter
from utility.data_retireve import get_current_alumni_data

router = APIRouter()

@router.get("/analytics/verification_status")
def verification_summary():
    data = get_current_alumni_data()
    alumni = data.get("data", [])

    total = len(alumni)
    verified_count = sum(1 for a in alumni if a.get("verified") == True)
    unverified_count = total - verified_count
    verified_percent = round((verified_count / total) * 100, 2) if total > 0 else 0
    unverified_percent = round((unverified_count / total) * 100, 2) if total > 0 else 0

    return {
        "total_alumni": total,

        "verified": {
            "count": verified_count,
            "percent": verified_percent
        },

        "unverified": {
            "count": unverified_count,
            "percent": unverified_percent
        },

        "summary_message": 
            f"{verified_count} alumni are verified and {unverified_count} are unverified."
    }
