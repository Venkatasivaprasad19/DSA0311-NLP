text = "John went home. He slept."
words = text.replace(".", "").split()
last_noun = None
for word in words:
    if word.istitle() and word.lower() not in ["he", "she", "it", "they"]:
        last_noun = word
    if word.lower() == "he":
       print(f"He refers to {last_noun}")
