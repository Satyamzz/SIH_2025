# Import the function we just made
import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from get_data import get_alumni_data

alumni_list = get_alumni_data()

if alumni_list:
    for alum in alumni_list[:5]: 
        name = alum.get("name", "Unknown")
        skills = alum.get("profileDetails", {}).get("skills", [])
        print(f"Processing: {name}")
else:
    print("No data available to process.")