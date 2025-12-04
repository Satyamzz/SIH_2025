import sys, os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from pydantic import BaseModel
from fastapi import APIRouter
from demo_data.alumni_data import get_demo_data
import spacy

class des(BaseModel):
    location: str

nlp = spacy.load("skill_ner_model")


router=APIRouter
@router.post("recommend/alum_for_event")
def recc(req:des):
    data=get_demo_data()
    doc=nlp(req)
    skills=[]
    doc=nlp()
    for ent in doc.ents:
        skills.append(ent.text)

    alumni=data["alumni"]
    for alum in alumni:
        skills=alum.get("skills","unknown")
        for skill in skills:
            

