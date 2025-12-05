"""
Generate skill embeddings for alumni data.
Creates embeddings for all skills and saves them with id, name, and skill embeddings.
"""

from sentence_transformers import SentenceTransformer
from alumni_data import get_demo
import numpy as np
import json

model = SentenceTransformer("intfloat/e5-small")


data = get_demo()
alumni = data['alumni']


all_skills = set()
alumni_info = []

for person in alumni:
    person_id = person['id']
    person_name = person['name']
    skills = person.get('skills', [])
    
    for skill in skills:
        all_skills.add(skill)
    
    alumni_info.append({
        'id': person_id,
        'name': person_name,
        'skills': skills
    })

all_skills = sorted(list(all_skills))
print(f"\nFound {len(all_skills)} unique skills:")
print(all_skills)

# Generate embeddings for all skills
print(f"\nGenerating embeddings for {len(all_skills)} skills...")
skill_embeddings = model.encode(all_skills, convert_to_numpy=True)

print(f"Embedding dimension: {skill_embeddings.shape[1]}")

# Create skill embedding mapping
skill_to_embedding = {skill: embedding.tolist() for skill, embedding in zip(all_skills, skill_embeddings)}

# Create alumni with skill embeddings
print("\nProcessing alumni data...")
alumni_with_embeddings = []

for person in alumni_info:
    person_id = person['id']
    person_name = person['name']
    skills = person['skills']
    
    # Get embeddings for this person's skills
    person_skill_embeddings = [skill_to_embedding[skill] for skill in skills]
    
    # Average the embeddings or keep them as a list
    if person_skill_embeddings:
        avg_embedding = np.mean(person_skill_embeddings, axis=0).tolist()
    else:
        avg_embedding = [0.0] * skill_embeddings.shape[1]
    
    alumni_with_embeddings.append({
        'id': person_id,
        'name': person_name,
        'skill_embedding': avg_embedding,
        'skills': skills  # Keep original skills for reference
    })

# Save to JSON
output_file = 'alumni_skill_embeddings.json'
print(f"\nSaving to {output_file}...")

with open(output_file, 'w') as f:
    json.dump({
        'alumni': alumni_with_embeddings,
        'metadata': {
            'model': 'intfloat/e5-small',
            'embedding_dimension': skill_embeddings.shape[1],
            'total_alumni': len(alumni_with_embeddings),
            'total_unique_skills': len(all_skills)
        }
    }, f, indent=2)

print(f"✓ Saved {len(alumni_with_embeddings)} alumni records with skill embeddings")

# Print sample
print("\n" + "="*80)
print("SAMPLE OUTPUT (First alumni):")
print("="*80)
sample = alumni_with_embeddings[0]
print(f"\nID: {sample['id']}")
print(f"Name: {sample['name']}")
print(f"Skills: {sample['skills']}")
print(f"Skill Embedding (first 10 dimensions): {sample['skill_embedding'][:10]}")
print(f"Embedding dimension: {len(sample['skill_embedding'])}")

print("\n" + "="*80)
print("SUMMARY:")
print("="*80)
print(f"✓ Total alumni processed: {len(alumni_with_embeddings)}")
print(f"✓ Total unique skills: {len(all_skills)}")
print(f"✓ Embedding dimension: {skill_embeddings.shape[1]}")
print(f"✓ Output file created:")
print(f"  - {output_file}")
