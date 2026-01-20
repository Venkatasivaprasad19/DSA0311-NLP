import spacy
nlp = spacy.load("en_core_web_sm")
doc = nlp("the apple is in califirnia")
for ent in doc.ents:
    print(ent.text, ent.label_)