from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
words = ["running","cars","jumping"]
for word in words:
    print(word,"->",lemmatizer.lemmatize(word))