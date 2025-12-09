import requests

def get_alumni_data():
    """
    Fetches live alumni data from the API.
    Returns: A list of alumni dictionaries, or an empty list if failed.
    """
    url = "https://sih-2025-user.onrender.com/api/v1/alumni/all"
    headers = {
        "x-analytics-api-key": "AnalyticsTopSecret"
    }

    try:
        print("⏳ Fetching live alumni data...")
        response = requests.get(url, headers=headers, timeout=60)

        if response.status_code == 200:
            json_response = response.json()
            # Validate structure before returning
            if json_response.get("success") and "data" in json_response:
                print(f"✅ Successfully loaded {len(json_response['data'])} alumni profiles.")
                return json_response["data"]
            else:
                print("⚠️ API returned 200 but data format was unexpected.")
                return []
        else:
            print(f"❌ Error: Server returned status {response.status_code}")
            return []

    except Exception as e:
        print(f"❌ Connection Failed: {e}")
        return []