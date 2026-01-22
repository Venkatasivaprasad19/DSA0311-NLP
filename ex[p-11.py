import nltk
grammar = nltk.CFG.fromstring("""
S -> NP VP
NP -> 'john'
VP -> 'runs'
""")
parser = nltk.ChartParser(grammar)
sentence = ["john","runs"]
for tree in parser.parse(sentence):
    print(tree)
    