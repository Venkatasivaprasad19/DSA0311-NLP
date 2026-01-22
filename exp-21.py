import nltk
sentence ="the cat eats fish"
tokens = nltk.word_tokenize(sentence)
tags = nltk.pos_tag(tokens)
nouns = [w for w,t in tags if t.startswith("NN")]
print(nouns)