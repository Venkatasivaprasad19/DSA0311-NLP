def rule_pos(word):
    if word.endswith("ing"):
        return "VBG"
    elif word.endswith("ed"):
        return "VBD"
    else:
        return "NN"
words=["running","jumped","jump"]
for word in words:
    print(word,rule_pos(word))