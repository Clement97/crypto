import string
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


#encrypt(inputPlainText(),inputKey())
encrypt('test',1)
decrypt('uftu',1)
