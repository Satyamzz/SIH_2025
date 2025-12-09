import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import json
import os
from huggingface_hub import InferenceClient
from dotenv import load_dotenv
from get_data import get_alumni_data
load_dotenv()
hf_token = os.getenv("HF_TOKEN")
hf_client = InferenceClient(token=hf_token)
data=get_alumni_data()
print(data)
def get_embedding(text_input):
 
    try:
       
        response = hf_client.feature_extraction(
            text=text_input,
            model="sentence-transformers/all-MiniLM-L6-v2"
        )
        
        if isinstance(response, list):
            return response if isinstance(response[0], float) else response[0]
        else:
            return response.tolist()

    except Exception as e:
        print(f"Error generating embedding: {e}")
        return []

def create_student_profile():
    print("--- 🎓 Create New Student Profile ---")
    
    # 1. Take Basic Inputs
    s_id = input("Enter Student ID (e.g., 21): ")
    dept = input("Enter Department (e.g., CSE): ")
    year = input("Enter Passout Year (e.g., 2025): ")
    
    # 2. Take Text Inputs
    skills_input = input("Enter Skills (comma separated, e.g., Python, SQL): ")
    hobbies_input = input("Enter Hobbies (comma separated, e.g., Cricket, Reading): ")
    
    print("\n⏳ Generating vectors with Hugging Face Client...")
    
    try:
        # 3. Generate Embeddings using the SDK function
        skills_vector = get_embedding(skills_input)
        hobbies_vector = get_embedding(hobbies_input)
        
        # Check if we actually got data back
        if not skills_vector or not hobbies_vector:
            raise ValueError("Empty vector returned from API")

        # 4. Construct the Final Data Structure
        student_data = {
            "_id": int(s_id),
            "department": dept,
            "passout_year": int(year),
            "skills_embedding": skills_vector,
            "hobbies_embedding": hobbies_vector,
            "skills_list": [s.strip() for s in skills_input.split(',')],
            "hobbies_list": [h.strip() for h in hobbies_input.split(',')]
        }
        
        print("\n✅ Data Constructed Successfully!")
        return student_data

    except Exception as e:
        print(f"\n❌ Failed to generate profile.\nError: {e}")
        return None

# # --- RUN THE CODE ---
# if __name__ == "__main__":
#     final_data = create_student_profile()
    
#     if final_data:
#         print("\n--- JSON PREVIEW (Ready for MongoDB) ---")
#         # Preview the first 5 dimensions just to prove it works
#         print(json.dumps({
#             "_id": final_data["_id"],
#             "skills": final_data["skills_list"],
#             "skills_vec_preview": final_data["skills_embedding"][:5]
#         }, indent=2))