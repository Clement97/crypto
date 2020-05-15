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
    french = {'A' : 9.42,'B' : 1.02,'C' : 2.64,'D' : 3.39,'E' : 15.87,'F' : 0.95,'G' : 1.04,'H' : 0.77,'I' : 8.41,'J' : 0.89,'K' : 0.00,'L' : 5.34,'M' : 3.24,'N' : 7.15,'O' : 5.14,'P' : 2.86,'Q' : 1.06,'R' : 6.46,'S' : 7.90,'T' : 7.26,'U' : 6.24,'V' : 2.15,'W' : 0.00,'X' : 0.30,'Y' : 0.24,'Z' : 0.32}

    text = cyphertext

    freq = french.copy()

    print(freq)
    for key in freq:
        freq[key] = 0.00

    for char in cyphertext:
        freq[char] = frequence(char, text)

    freq = OrderedDict(sorted(freq.items(), key=lambda t: t[1], reverse=True))

    print(freq)
    for key in freq:
        print (key + ' -> ' + str(freq.get(key) * 100))

    frenchSorted = OrderedDict(sorted(french.items(), key=lambda t: t[1], reverse=True))

    possibleKeys = []
    for i,key in enumerate(freq):
        if(i<3):
            maxKey = getMaxValueKey(french)
            possibleKeys.append( ((26+ord(key)-65) -ord(maxKey)-65)%26)

    indexKey = -1
    errorMin = 99999999999
    for possibleKey in possibleKeys:
        plainfreq = {}
        for i,key in enumerate(freq):
            plainfreq[chr((ord(key)-65+possibleKey)%26+65)]=freq[key]
        errorCompute = compare_dict(frenchSorted,plainfreq)
        if(errorMin>errorCompute):
            errorMin = errorCompute
            indexKey = possibleKeys.index(possibleKey)

    code_cesar(cyphertext,possibleKeys[indexKey])


def compare_dict(dic1,dic2):
    sum = 0
    for i,key in enumerate(dic1):
        sum += (dic1[key]-dic2[key])**2
    return sum
def getMaxValueKey(dic):
    v=list(dic.values())
    k=list(dic.keys())
    return k[v.index(max(v))]

def frequence(letter, text):            
    return text.count(letter) / len(text)

def testFA():
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

testFA()
