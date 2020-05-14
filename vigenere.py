def code_vigenere (text, key, decode = False) :
    cyphertext = ""
    for i,c in enumerate(text) :
        d = key[ i % len(key) ]
        d = ord(d) - 65
        if decode : 
            d = 26 - d
        cyphertext += chr((ord(c)-65+d)%26+65)
    print(cyphertext)
    return cyphertext

def DecodeVigenere(cyphertext, key):
    return code_vigenere(cyphertext, key, True)

def CodeVigenere(plaintext, key):
    return code_vigenere(plaintext, key)

def PGCD (m,n) :
    if m <= 0 or n <= 0 : raise Exception("impossible de calculer le PGCD")
    if m == 1 or n == 1 : return 1
    if m == n : return m
    if m < n : return PGCD (m, n-m)
    return PGCD (n, m-n)


# code_vigenere('TEST','CLE')
# code_vigenere('VPWV','CLE',True)