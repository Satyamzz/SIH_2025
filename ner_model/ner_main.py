import spacy
from fastapi import APIRouter
from pydantic import BaseModel
nlp = spacy.load("skill_ner_model")

class Desc(BaseModel):
    desc: str

router=APIRouter()
@router.post("/ner_skill")
def extract_skill(req:Desc):
    doc = nlp(req.desc)
    skills=[]
    for ent in doc.ents:
        if ent.label_=="SKILL":
            skills.append(ent.text)
    return {
        "no of skills": len(skills),
        "skills": skills
    }
    
    