import json

with open("recommendation_system/realistic_skill_ner_1000_tuple.json", "r") as f:
    raw_data = json.load(f)

TRAIN_DATA = []

for item in raw_data:
    text = item[0]            
    entities = item[1]["entities"]
    TRAIN_DATA.append((text, {"entities": entities}))
