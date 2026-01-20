import nltk
grammar = nltk.PCFG.fromstring("""
S -> NP VP [1.0]
NP -> 'dogs' [0.5] | 'cats' [0.5]
VP -> 'run' [1.0]
""")
parser= nltk.ViterbiParser(grammar)
sentence =["dogs","run"]
for tree in parser.parse(sentence):
    print(tree)