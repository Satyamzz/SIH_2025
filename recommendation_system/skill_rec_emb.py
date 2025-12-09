import sys, os
import numpy as np
import json
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List, Dict
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
from huggingface_hub import InferenceClient

load_dotenv()


class SKILL(BaseModel):
    skills: List[str]

hf_token = os.getenv("HF_TOKEN")
if not hf_token:
    print("WARNING: HF_TOKEN is missing. API calls will likely fail.")

hf_client = InferenceClient(model="sentence-transformers/all-MiniLM-L6-v2", token=hf_token)

json_path = os.path.join(os.path.dirname(__file__), "..", "demo_data", "alumni_skill_embeddings.json")

try:
    with open(json_path, 'r') as f:
        skill_embeddings_data = json.load(f)
    
    alumni_matrix = np.array([item["skill_embedding"] for item in skill_embeddings_data["alumni"]])
    alumni_ids = [item.get("id", "unknown") for item in skill_embeddings_data["alumni"]]
    
    print(f"Loaded {len(alumni_ids)} alumni embeddings into memory.")

except FileNotFoundError:
    print(f"ERROR: Could not find embedding file at {json_path}")
    alumni_matrix = np.array([])
    alumni_ids = []

router = APIRouter()

@router.post("/recommend/alum_emb")
def recommend(req: SKILL):
    skills = req.skills
    
    # Basic Validation
    if not skills:
        return {"error": "No skills provided", "recommendations": {}}
    
    # Safety check: If DB failed to load, return error
    if alumni_matrix.size == 0:
        raise HTTPException(status_code=503, detail="Alumni database not loaded.")

    # --- 2. ACCURACY: Query Formatting ---
    formatted_skills = [f"query: {s}" for s in skills]

    try:
        # Get embeddings
        # Note: We rely on numpy operations directly for speed
        skill_vectors = hf_client.feature_extraction(formatted_skills)
        
        # Ensure it is a numpy array (HF sometimes returns lists)
        skill_vectors = np.array(skill_vectors)

        # Average into one "User Profile Vector" (1, 384)
        skill_vector_avg = np.mean(skill_vectors, axis=0).reshape(1, -1)

        # --- 3. MATH: Matrix Multiplication ---
        # Cosine Similarity: (A . B) / (||A|| * ||B||)
        # sklearn handles the normalization if vectors aren't normalized. 
        # Ideally, if stored vectors are already normalized, just use np.dot for 10x speed.
        sim_scores = cosine_similarity(skill_vector_avg, alumni_matrix)[0]

        # Zip, Sort, and Slice
        # Using a heap is faster for top-k if N > 10,000, but sort is fine for small N
        results = list(zip(alumni_ids, sim_scores))
        results.sort(key=lambda x: x[1], reverse=True)

        # Format output
        sorted_scores = {r[0]: float(r[1]) for r in results[:10]}

        return {
            "input_skills": skills,
            "recommendations": sorted_scores
        }

    except Exception as e:
        print(f"Inference Error: {e}")
        raise HTTPException(status_code=500, detail=f"Error generating embeddings: {str(e)}")