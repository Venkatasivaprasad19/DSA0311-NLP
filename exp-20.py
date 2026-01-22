from sklearn.feature_extraction.text import TfidfVectorizer
docs = ["i love NLP","NLP is easy","i love python"]
vectorizer = Tfidfvectorizer()
tfidf = vectorizer.fit_transform(docs)
print(tfidf.toarray)