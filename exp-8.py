import random
words=["boy","running","blue"]
tags=["NN","VB","JJ"]
for word in words:
    print(word, random.choice(tags))