import spacy

nlp = spacy.load("skill_ner_model")

text = """"The Computer Science Society is hosting a hands-on workshop on Django, the popular Python web framework used to build scalable web applications. This event will introduce students to essential concepts including URL routing, views, templates, and database modeling with Django’s ORM. Participants will work on creating a functional mini web application by the end of the session. Senior alumni working as full stack developers will also share insights on deploying Django projects using modern cloud platforms. The workshop is open to beginners and aims to help students understand real-world use cases of Django in industry-level product development"""

doc = nlp(text)

for ent in doc.ents:
    print(ent.text, "->", ent.label_)
