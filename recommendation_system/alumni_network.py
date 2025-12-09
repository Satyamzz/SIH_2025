import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from get_data import get_alumni_data

router = APIRouter()

class TravelRequest(BaseModel):
    userId: str
    travelCity: str

def normalize(text):
    """Normalize text for comparison"""
    return text.lower().strip() if text else ""

def get_city(location_data):
    """Extract and normalize city from location data"""
    if not location_data:
        return None
    
    if isinstance(location_data, dict):
        city = location_data.get("city", "")
    elif isinstance(location_data, str):
        city = location_data.split(',')[0]
    else:
        return None
    
    return normalize(city) if city else None

def build_match_reason(year_diff, target_year, is_same_dept, dept):
    """Build match reason description"""
    reasons = []
    
    if year_diff == 0:
        reasons.append(f"Same Batch ({target_year})")
    elif year_diff <= 2:
        reasons.append(f"{year_diff} year gap")
    else:
        reasons.append(f"Graduated {target_year}")
    
    if is_same_dept:
        reasons.append(f"Same Dept ({dept})")
    
    return ", ".join(reasons)

def find_alumni_by_id(alumni_list, user_id):
   
    for alumni in alumni_list:
        if alumni.get("_id") == user_id:
            return alumni
    return None

@router.post("/recommend/travel")
def recommend_for_travel(request: TravelRequest):
    """
    Recommend alumni in the city the user is traveling to.
    Only requires userId and travelCity.
    """
    travel_city = normalize(request.travelCity)
    
    if not travel_city:
        raise HTTPException(status_code=400, detail="Travel city is required")
    
    # Get all alumni data
    all_alumni = get_alumni_data()
    if not all_alumni:
        raise HTTPException(status_code=404, detail="No alumni data found")
    
    # Find the requesting user
    user = find_alumni_by_id(all_alumni, request.userId)
    if not user:
        raise HTTPException(status_code=404, detail=f"User with ID {request.userId} not found")
    
    # Get user profile
    user_profile = user.get("profileDetails")
    if not user_profile or not isinstance(user_profile, dict):
        raise HTTPException(status_code=400, detail="User profile is incomplete")
    
    target_year = user_profile.get("graduationYear")
    target_dept = normalize(user_profile.get("department", ""))
    
    if not target_year:
        raise HTTPException(status_code=400, detail="User graduation year is required")
    
    recommendations = []
    
    for peer in all_alumni:
        # Skip self
        if peer.get("_id") == request.userId:
            continue
        
        # Ensure peer and profile exist
        if not peer or not isinstance(peer, dict):
            continue
        
        profile = peer.get("profileDetails")
        if not profile or not isinstance(profile, dict):
            continue
        
        peer_city = get_city(profile.get("location"))
        if peer_city != travel_city:
            continue
        
        peer_year = profile.get("graduationYear")
        if peer_year is None:
            continue
        
        peer_dept = normalize(profile.get("department", ""))
        year_diff = abs(target_year - peer_year)
        is_same_dept = (peer_dept == target_dept)
        
        recommendations.append({
            "id": peer.get("_id"),
            "name": peer.get("name"),
            "email": peer.get("email"),
            "graduationYear": peer_year,
            "department": profile.get("department"),
            "company": profile.get("currentCompany", "Not Specified"),
            "designation": profile.get("designation", "Not Specified"),
            "match_reason": build_match_reason(
                year_diff, target_year, is_same_dept, 
                profile.get("department")
            ),
            "year_diff": year_diff,
            "is_same_dept": is_same_dept
        })
    
    recommendations.sort(key=lambda x: (
        x['year_diff'] > 2,  
        not x['is_same_dept'],  
        x['year_diff'] 
    ))
    
    return {
        "userId": request.userId,
        "userName": user.get("name"),
        "travelCity": travel_city.title(),
        "userDetails": {
            "graduationYear": target_year,
            "department": user_profile.get("department")
        },
        "totalMatches": len(recommendations),
        "recommendations": recommendations
    }