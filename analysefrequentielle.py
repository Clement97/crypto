from collections import OrderedDict

def getMaxValueKey(dic):
    v=list(dic.values())
    k=list(dic.keys())
    return k[v.index(max(v))]

def frequence(letter, text):            
    return text.count(letter) / len(text)

french = {'a' : 9.42,'b' : 1.02,'c' : 2.64,'d' : 3.39,'e' : 15.87,'f' : 0.95,'g' : 1.04,'h' : 0.77,'i' : 8.41,'j' : 0.89,'k' : 0.00,'l' : 5.34,'m' : 3.24,'n' : 7.15,'o' : 5.14,'p' : 2.86,'q' : 1.06,'r' : 6.46,'s' : 7.90,'t' : 7.26,'u' : 6.24,'v' : 2.15,'w' : 0.00,'x' : 0.30,'y' : 0.24,'z' : 0.32}

text = 'segelazew aop qj lnkfap z ajyuyhklazea cnwpqepa aynepa ykklanwperaiajp'

freq = french.copy()

for key in freq:
    freq[key] = 0.00

for char in text.replace(' ', ''):
    freq[char] = frequence(char, text)

freq = OrderedDict(sorted(freq.items(), key=lambda t: t[1], reverse=True))

for key in freq:
    print (key + ' -> ' + str(freq.get(key) * 100))

frenchSorted = OrderedDict(sorted(french.items(), key=lambda t: t[1], reverse=True))

#https://fr.wikipedia.org/wiki/Analyse_fréquentielle

for key in freq:
    if freq.get(key) != 0.00:
        maxKey = getMaxValueKey(french)
        del french[maxKey]
        print('Key => ' + key + ', maxKey => ' + maxKey)
        text = text.replace(key, maxKey)

print(text)
