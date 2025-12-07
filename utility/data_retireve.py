import requests

# Configuration
API_URL = "https://sih-2025-user.onrender.com/api/v1/alumni/all"
HEADERS = {
    "x-analytics-api-key": "AnalyticsTopSecret"
}

def get_current_alumni_data():
    try:
        response = requests.get(API_URL, headers=HEADERS, timeout=10)
        
        if response.status_code == 200:
            return response.json()
        else:
            # Log the error internally so you can debug later
            print(f"[Error] API returned status: {response.status_code}")
            return []
            
    except requests.exceptions.RequestException as e:
        print(f"[Error] Connection failed: {e}")
        return []