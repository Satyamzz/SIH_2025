import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
import json
import os
from huggingface_hub import InferenceClient  # Fixed import
from dotenv import load_dotenv
# 1. Configuration
load_dotenv()
INPUT_FILE = 'data_for_mongo/alumni'
OUTPUT_FILE = 'alumni_embeddings.json'

# Load token
hf_token = os.getenv("HF_TOKEN")

# Initialize the client (Standard way to use Hugging Face API)
hf_client = InferenceClient(model="sentence-transformers/all-MiniLM-L6-v2", token=hf_token)

def main():
    # 2. Load the Data
    try:
        with open(INPUT_FILE, 'r') as f:
            alumni_data = json.load(f)
        print(f"Loaded {len(alumni_data)} alumni records.")
    except FileNotFoundError:
        print(f"Error: Could not find {INPUT_FILE}")
        return

    # 3. Pre-process Data (Extract IDs and format Skills)
    ids_to_process = []
    texts_to_embed = []

    for person in alumni_data:
        # Handle MongoDB specific ID format {"$oid": "..."} or standard string
        raw_id = person.get('userId')
        if isinstance(raw_id, dict) and '$oid' in raw_id:
            user_id = raw_id['$oid']
        else:
            user_id = raw_id

        # Convert skills array to a single string for embedding
        skills = person.get('skills', [])
        if skills:
            skills_str = ", ".join(skills)
        else:
            # If no skills, we use a placeholder or skip. 
            # Using a placeholder ensures ID count matches embedding count.
            skills_str = "General professional" 
        
        ids_to_process.append(user_id)
        texts_to_embed.append(skills_str)

    # 4. Get Embeddings
    batch_size = 20
    all_embeddings = []

    print("Generating embeddings...")

    for i in range(0, len(texts_to_embed), batch_size):
        batch_texts = texts_to_embed[i : i + batch_size]
        
        try:
            # Uses the InferenceClient to fetch embeddings directly
            # This handles the API URL and Headers automatically
            response = hf_client.feature_extraction(batch_texts)
            
            # response is usually a numpy array or list of lists. 
            # We ensure it is a standard list for JSON serialization.
            if hasattr(response, 'tolist'):
                batch_embeddings = response.tolist()
            else:
                batch_embeddings = response

            all_embeddings.extend(batch_embeddings)
            print(f"Processed batch {i} to {i + len(batch_texts)}")

        except Exception as e:
            print(f"Error processing batch starting at index {i}: {e}")

    # 5. Construct Final JSON
    final_output = []

    if len(ids_to_process) == len(all_embeddings):
        for uid, emb in zip(ids_to_process, all_embeddings):
            final_output.append({
                "userId": uid,
                "embedding": emb
            })
    else:
        print(f"Warning: ID count ({len(ids_to_process)}) does not match Embedding count ({len(all_embeddings)}).")

    # 6. Save to File
    try:
        with open(OUTPUT_FILE, 'w') as f:
            json.dump(final_output, f, indent=2)
        print(f"Successfully saved {len(final_output)} records to {OUTPUT_FILE}")
    except Exception as e:
        print(f"Error saving file: {e}")

if __name__ == "__main__":
    if not hf_token:
        print("Error: HF_TOKEN environment variable is not set.")
    else:
        main()