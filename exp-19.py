from nltk.wsd import lesk
sentence ="i went to bank to deposit money"
sense = lesk(sentence.split(), "bank")
print(sense.definition())