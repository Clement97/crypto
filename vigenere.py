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


code_vigenere('TEST','CLE')
code_vigenere('VPWV','CLE',True)