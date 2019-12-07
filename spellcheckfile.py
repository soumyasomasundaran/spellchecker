import string
from spellchecker import SpellChecker

def spellchecking(filename):
    spell = SpellChecker()
    total = lc = wc = 0
    i=0
    lci=[]
    wci=[]
    wordi=[]
    with open(filename, "r") as f:
        for line in f:
            line = (line.translate(str.maketrans('', '', string.punctuation)))  # Remove punctuation from a string
            lc += 1
            wc=0
            for word in line.split():
                wc += 1
                if not spell[word]:
                    total = total + 1
                    wordi.append(word)
                    lci.append(lc)
                    wci.append(wc)
    return (total,wordi,lci,wci,)

