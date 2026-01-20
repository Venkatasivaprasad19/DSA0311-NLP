import random
text="i love NLP i understand NLP"
words=text.split()
bigrams=list(zip(words,words[1:]))
print(random.choice(bigrams))