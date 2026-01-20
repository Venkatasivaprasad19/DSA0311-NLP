def plural(noun):
    if noun.endswith('y'):
        return noun [:-1] + 'ies'
    else:
        return noun + 's'
words = ["city","car"]
for word in words:
    print("plural form:",plural(word))