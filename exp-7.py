import nltk
sentence="i am running"
tokens=nltk.word_tokenize(sentence)
tags=nltk.pos_tag(tokens)
print(tags)