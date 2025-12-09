# from training_data import TRAIN_DATA
# import spacy
# from spacy.training.example import Example
# from spacy.util import minibatch, compounding
# import random

# nlp = spacy.load("en_core_web_sm")  
# ner = nlp.get_pipe("ner")

# ner.add_label("SKILL")
# unaffected_pipes = [pipe for pipe in nlp.pipe_names if pipe != "ner"]

# with nlp.disable_pipes(*unaffected_pipes):
#     optimizer = nlp.resume_training()
#     for epoch in range(50): 
#         random.shuffle(TRAIN_DATA)
#         losses = {}
#         batches = minibatch(TRAIN_DATA, size=compounding(4.0, 32.0, 1.5))
#         for batch in batches:
#             for text, annotations in batch:
#                 doc = nlp.make_doc(text)
#                 example = Example.from_dict(doc, annotations)
#                 nlp.update([example], drop=0.2, losses=losses)
        
#         print(f"Epoch {epoch+1} Loss: {losses}")

# nlp.to_disk("skill_ner_model")
# print("Model saved as skill_ner_model")