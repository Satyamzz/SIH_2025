import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from pydantic import BaseModel
from fastapi import APIRouter
import json
import spacy
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
from sentence_transformers import SentenceTransformer

class SKILL(BaseModel):
    skill: str
nlp = spacy.load("skill_ner_model")
with open(os.path.join(os.path.dirname(__file__), "..", "demo_data", "alumni_skill_embeddings.json"), 'r') as f:
    skill_embeddings_data = json.load(f)
router = APIRouter()
model = SentenceTransformer("intfloat/e5-small")

@router.post("/recommend/alum_emb")
def recommend(req: SKILL):
    doc = nlp(req.location)
    skills = [ent.text for ent in doc.ents]
    if not skills:
        return {"error": "No skills found in text"}
    skill_vectors = model.encode(skills)
    skill_vector_avg = np.mean(skill_vectors, axis=0).reshape(1, -1)
    alumni = skill_embeddings_data["alumni"]
    scores = {}

    for alum in alumni:
        alum_id = alum.get("id", "unknown")
        alum_vector = np.array(alum["skill_embedding"]).reshape(1, -1)
        sim = cosine_similarity(skill_vector_avg, alum_vector)[0][0]
        scores[alum_id] = float(sim)

    sorted_scores = dict(sorted(scores.items(), key=lambda x: x[1], reverse=True))
    return {
        "input_skills": skills,
        "recommendations": sorted_scores
    }
