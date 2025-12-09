from fastapi import APIRouter
from utility.data_retireve import get_current_alumni_data

router = APIRouter()

def safe_percent(value):
    try:
        return int(value) if value is not None else 0
    except:
        return 0

@router.get("/analytics/account_completion")
def account_completion_analytics():
    raw = get_current_alumni_data()

    # Extract list of alumni
    data = raw.get("data", [])
    if not data:
        return {"error": "No alumni data found"}

    completion_values = [
        safe_percent(a.get("completion_percent")) for a in data if a
    ]

    total = len(completion_values)
    avg_completion = round(sum(completion_values) / total, 2)

    distribution = {
        "60-70": len([x for x in completion_values if 60 <= x < 70]),
        "70-80": len([x for x in completion_values if 70 <= x < 80]),
        "80-90": len([x for x in completion_values if 80 <= x < 90]),
        "90-100": len([x for x in completion_values if 90 <= x <= 100]),
    }

    sorted_alumni = sorted(
        data,
        key=lambda x: safe_percent.get("profileCompletion"),
        reverse=True
    )

    top_5 = sorted_alumni[:5]

    bottom_5_list = sorted_alumni[-5:]
    bottom_5 = sorted(
        bottom_5_list,
        key=lambda x: safe_percent(x.get("completion_percent")),
        reverse=True
    )

    fully_complete = len([x for x in completion_values if x >= 90])
    incomplete = total - fully_complete

    return {
        "total_alumni": total,
        "average_completion_percent": avg_completion,
        "completion_distribution": distribution,
        "fully_completed_profiles": fully_complete,
        "incomplete_profiles": incomplete,
        "top_5_profiles": top_5,
        "bottom_5_profiles": bottom_5,
    }
