import json
import os

json_path = os.path.join(os.path.dirname(__file__),"alumni_embeddings.json")

if not os.path.exists(json_path):
    print(f"File not found: {json_path}")
else:
    with open(json_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        print(f"Length of data in {os.path.basename(json_path)}: {len(data)}")