import string
from collections import OrderedDict

alphaInit = string.printable

def inputPlainText():
    print("Entrez votre phrase à chiffrer")
    return input()

def inputKey():
    key = -1 
    while (key<0) or (key>25):
        print("Entrez votre clé de chiffrement")
        key = int(input())
        return key


###############César avec + de Lettre min/maj et divers char ASCII#####################
def encrypt(plaintext,key):
    print('CHIFFREMENT')
    phraseAChiffrer = plaintext
    print('votre phrase à chiffrer')
    print(phraseAChiffrer)

    cle = key
    phraseChiffree = ''
    for lettre in phraseAChiffrer:
        lettreEnChiffreAC = alphaInit.index(lettre)
        lettreChiffreeCleAC = (lettreEnChiffreAC + cle) % len(alphaInit)
        lettreChiffreeAC = alphaInit[lettreChiffreeCleAC]
        phraseChiffree = phraseChiffree + lettreChiffreeAC
    print('votre phrase chiffrée')
    print(phraseChiffree)

def decrypt(cyphertext,key):
    print('DECHIFFREMENT')
    print('votre phrase à déchiffrer')
    phraseChiffree=cyphertext
    print(phraseChiffree)
    cle = key
    phraseDechiffree = ''
    for lettre in phraseChiffree:
        lettreEnChiffreAD = alphaInit.index(lettre)
        lettreChiffreeCleAD = (lettreEnChiffreAD - cle) % len(alphaInit)
        lettreChiffeeAD = alphaInit[lettreChiffreeCleAD]
        phraseDechiffree = phraseDechiffree + lettreChiffeeAD
    print('votre phrase déchiffrée')
    print(phraseDechiffree)

###############César avec seulement lettre MAJ#####################

def code_cesar (text, key, decode = False) :
    cyphertext = ""
    keycp = key
    for i,c in enumerate(text) :
        if decode : 
            keycp = 26 - key
        cyphertext += chr((ord(c)-65+keycp)%26+65)
    print(cyphertext)
    return cyphertext

def DecodeCesar(cyphertext, key):
    return code_cesar(cyphertext, key, True)

def CodeCesar(plaintext, key):
    return code_cesar(plaintext, key)

###############Analyse fréquentielle#####################

def decryptbyFA(cyphertext):
    french = {'a' : 9.42,'b' : 1.02,'c' : 2.64,'d' : 3.39,'e' : 15.87,'f' : 0.95,'g' : 1.04,'h' : 0.77,'i' : 8.41,'j' : 0.89,'k' : 0.00,'l' : 5.34,'m' : 3.24,'n' : 7.15,'o' : 5.14,'p' : 2.86,'q' : 1.06,'r' : 6.46,'s' : 7.90,'t' : 7.26,'u' : 6.24,'v' : 2.15,'w' : 0.00,'x' : 0.30,'y' : 0.24,'z' : 0.32}

    text = cyphertext

    freq = french.copy()

    for key in freq:
        freq[key] = 0.00

    for char in text.replace(' ', ''):
        freq[char] = frequence(char, text)

    freq = OrderedDict(sorted(freq.items(), key=lambda t: t[1], reverse=True))

    for key in freq:
        print (key + ' -> ' + str(freq.get(key) * 100))

    frenchSorted = OrderedDict(sorted(french.items(), key=lambda t: t[1], reverse=True))


    for key in freq:
        if freq.get(key) != 0.00:
            maxKey = getMaxValueKey(french)
            del french[maxKey]
            print('Key => ' + key + ', maxKey => ' + maxKey)
            text = text.replace(key, maxKey)

    print(text)
    return text

def getMaxValueKey(dic):
    v=list(dic.values())
    k=list(dic.keys())
    return k[v.index(max(v))]

def frequence(letter, text):            
    return text.count(letter) / len(text)

def test():
    text = open("input.txt", "r")
    message = text.read()
    message = message.replace ("\n", "").replace ("\r", "").replace ("\t", "").replace (" ", "").replace (",", "")
    message = message.replace (";", "").replace (":", "").replace (".", "").replace ("'", "").replace ("\"", "")
    message = message.replace ("-", "").replace ("!", "").replace ("?", "").replace ("(", "").replace (")", "").replace("=","")
    message = message.upper ()
    print(message)
    code = CodeCesar(message,6)
    decryptbyFA(code)

# encrypt(inputPlainText(),inputKey())
# encrypt('TEST',12)
# code_cesar('ABCD',1)
# code_cesar('BCDE',1,True)

# decrypt('uftu',1)

test()
