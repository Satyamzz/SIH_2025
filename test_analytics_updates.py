
import sys
import os
import json
from unittest.mock import MagicMock

# Add project root to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

# Mock data_retireve
import utility.data_retireve
mock_data = {
    "data": [
        {
            "_id": "693771922ae272cc600aa7db",
            "userId": "693771922ae272cc600aa7d9",
            "verified": False,
            "graduationYear": 2022,
            "degreeUrl": "https://storage.googleapis.com/degrees/satyam_singh_22.pdf",
            "skills": ["React", "Node.js", "MongoDB", "AWS"],
            "designation": "Senior Software Engineer",
            "company": "Wipro",
            "location": "Chennai, India",
            "phone": "+91 6541848016",
            "linkedin": "https://linkedin.com/in/satyam-singh",
            "branch": "Information Technology",
            "completion_percent": 100
        },
        {
            "_id": "dummy2",
            "verified": True,
            "graduationYear": 2023,
            "skills": ["Python", "Django"],
            "company": "Google",
            "location": "Bangalore, India",
            "branch": "Computer Science",
            "completion_percent": 80
        },
        None # Test robustness against None
    ]
}

utility.data_retireve.get_current_alumni_data = MagicMock(return_value=mock_data)

# Import functions to test
from analytics_services.admin_side.completion_stats import account_completion_analytics
from analytics_services.admin_side.skill_stats import skillfilter
from analytics_services.admin_side.get_companies import get_company_distribution
from analytics_services.admin_side.get_locations import get_company_distribution as get_location_distribution # Alias to avoid name clash
from analytics_services.admin_side.get_branch_distribution import get_branch_distribution
from analytics_services.admin_side.total_verified import verification_summary
from analytics_services.admin_side.summarize import alumni_analytics

def run_tests():
    print("Running Verification Tests...")
    
    try:
        print("\nTesting completion_stats...")
        res = account_completion_analytics()
        print("Result:", res)
    except Exception as e:
        print("FAILED completion_stats:", e)

    try:
        print("\nTesting skill_stats...")
        res = skillfilter()
        print("Result:", res)
    except Exception as e:
        print("FAILED skill_stats:", e)

    try:
        print("\nTesting get_companies...")
        res = get_company_distribution()
        print("Result:", res)
    except Exception as e:
        print("FAILED get_companies:", e)

    try:
        print("\nTesting get_locations...")
        res = get_location_distribution()
        print("Result:", res)
    except Exception as e:
        print("FAILED get_locations:", e)

    try:
        print("\nTesting get_branch_distribution...")
        res = get_branch_distribution()
        print("Result:", res)
    except Exception as e:
        print("FAILED get_branch_distribution:", e)

    try:
        print("\nTesting total_verified...")
        res = verification_summary()
        print("Result:", res)
    except Exception as e:
        print("FAILED total_verified:", e)

    try:
        print("\nTesting summarize...")
        res = alumni_analytics()
        print("Result:", res)
    except Exception as e:
        print("FAILED summarize:", e)

if __name__ == "__main__":
    run_tests()
