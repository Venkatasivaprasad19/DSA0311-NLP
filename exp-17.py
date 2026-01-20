from nltk.corpus import wordnet
synsets = wordnet.synsets("school")
for s in synsets:
    print(s.definition())