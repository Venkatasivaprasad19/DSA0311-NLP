from nltk.stem import PorterStemmer
ps = PorterStemmer()
words = ["walking","jumping"]
for word in words:
    print(word,"->",ps.stem(word))