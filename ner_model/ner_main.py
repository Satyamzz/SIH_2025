import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), " ")))
import spacy
from fastapi import APIRouter
from pydantic import BaseModel
current_dir = os.path.dirname(os.path.abspath(__file__))

# 2. Build the absolute path to the model folder
model_path = os.path.join(current_dir, "skill_ner_model")
nlp = spacy.load(model_path)

class Desc(BaseModel):
    desc: str

router=APIRouter()
@router.post("/ner_skill")
def extract_skill(req:Desc):
    doc = nlp(req.desc.lower())
    skills=[]
    for ent in doc.ents:
        if ent.label_=="SKILL":
            skills.append(ent.text)
    return {
        "no of skills": len(skills),
        "skills": skills
    }
    
    