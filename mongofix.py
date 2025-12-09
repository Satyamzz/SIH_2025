import requests
import random
import time
from faker import Faker

# --- CONFIGURATION ---
API_URL = "https://sih-2025-user.onrender.com/api/v1/auth/register/alumni"
HEADERS = {
    "Authorization":"bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY5MzJjZGJlYWQ2NTU4ZjgwN2Y3YzBjNiIsIm5hbWUiOiJTdC4gSnVkZSdzIENvbGxlZ2UgQWRtaW5pc3RyYXRpb24iLCJlbWFpbCI6InN0anVkZXMuYWRtaW4yQGV4YW1wbGUuY29tIiwiYWRkcmVzcyI6eyJzdHJlZXQiOiI0NS1BLCBOZWhydSBNYXJnIiwiY2l0eSI6Ik11bWJhaSIsInN0YXRlIjoiTWFoYXJhc2h0cmEiLCJjb3VudHJ5IjoiSW5kaWEifSwicGhvbmUiOiIrOTE5ODc2NTQzMjEwIiwiaWF0IjoxNzY1MjQwNjQyfQ.Vv6D37I4l3xoP42DzY7DNcQKgYVFEE7uwXhTq9x-awY"

}

fake = Faker('en_IN')

# --- 1. YOUR SPECIFIC NAMES ---
SPECIFIC_NAMES = [
    "Satyam Singh", "Rewant Bhriguvanshi", "Garvit Gupta", "Gurhans Grover", 
    "Krishna Yadav", "Shubhika Sinha", "Prayas Sharma", "Rohan Verma", 
    "Aditya Malhotra", "Sanya Kapoor", "Arjun Mehta", "Ishaan Bhat"
]

# --- 2. DATA POOLS ---
BRANCHES = ["Computer Science", "Information Technology", "Electronics", "Mechanical", "Civil"]
DESIGNATIONS = ["Senior Software Engineer", "Product Manager", "Data Scientist", "System Architect", "DevOps Engineer"]
COMPANIES = ["Tech Solutions Inc.", "Google", "Amazon", "Microsoft", "Infosys", "Wipro", "TCS"]
SKILLS_POOL = ["React", "Node.js", "MongoDB", "AWS", "Python", "Docker", "Kubernetes", "Java", "C++"]
LOCATIONS = ["Bangalore, India", "Mumbai, India", "Delhi, India", "Pune, India", "Hyderabad, India", "Chennai, India"]

# --- HELPER: Random Vector ---
def generate_vector():
    return [random.uniform(-1.0, 1.0) for _ in range(384)]

# --- MAIN GENERATOR ---
def generate_flat_alumni(total_count=46):
    print(f"--- 🚀 Sending {total_count} records (FLAT Structure) ---")

    for i in range(total_count):
        # A. Get Name
        if i < len(SPECIFIC_NAMES):
            full_name = SPECIFIC_NAMES[i]
            parts = full_name.split()
            first_name = parts[0]
            last_name = parts[1] if len(parts) > 1 else "Kumar"
        else:
            first_name = fake.first_name()
            last_name = fake.last_name()
            full_name = f"{first_name} {last_name}"

        # B. Generate Dynamic Values
        username = f"{first_name.lower()}_{fake.word()}_{random.randint(10,99)}"
        branch = random.choice(BRANCHES)
        
        # C. Construct Payload (EXACTLY YOUR STRUCTURE)
        payload = {
            "name": full_name,
            "username": username,
            "email": f"{first_name.lower()}.{last_name.lower()}{random.randint(100,999)}@example.com",
            "password": "SecurePassword123!",
            "collegeId": "6932cdbead6558f807f7c0c6", # Kept static as per your sample
            "graduationYear": random.randint(2019, 2024),
            "degreeUrl": f"https://storage.googleapis.com/degrees/{username}.pdf",
            "branch": branch,
            "skills": random.sample(SKILLS_POOL, k=4),
            "designation": random.choice(DESIGNATIONS),
            "company": random.choice(COMPANIES),
            "location": random.choice(LOCATIONS), # Kept as String, not Object
            "phone": f"+91 {random.randint(6000000000, 9999999999)}",
            "linkedin": f"https://linkedin.com/in/{first_name.lower()}-{last_name.lower()}",
            
            # Appending vector fields at the root level (required for your project)
            "embedding": generate_vector(),
            "vector_size": 384
        }

        # D. Send to API
        try:
            print(f"📤 [{i+1}/{total_count}] Sending {full_name}...")
            response = requests.post(API_URL, json=payload, headers=HEADERS, timeout=60)
            
            if response.status_code in [200, 201]:
                print("   ✅ Success")
            else:
                print(f"   ❌ Failed: {response.status_code} - {response.text}")
                
        except Exception as e:
            print(f"   ❌ Error: {e}")
            
        time.sleep(0.3)

if __name__ == "__main__":
    generate_flat_alumni(46)