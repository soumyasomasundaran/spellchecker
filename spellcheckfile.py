from spellchecker import SpellChecker
import string

spell = SpellChecker()
def spellchecking(filename):
    spell =SpellChecker()
    total = lc = wc = 0
    i=0
    linecountlist=[]
    wordcountlist=[]
    wordlist = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = (line.translate(str.maketrans('', '', string.punctuation)))  # Remove punctuation from a string
                lc += 1
                wc=0
                for word in line.split():
                    wc += 1
                    if not spell[word]:
                        total = total + 1
                        wordlist.append(word)
                        linecountlist.append(lc)
                        wordcountlist.append(wc)
        return (total,wordlist,linecountlist,wordcountlist)
    except IOError:
        return False
