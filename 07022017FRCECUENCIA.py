## Diana Bonilla
## Frecuencia de una palabra
## Python 2.7
## 07/02/2017

import nltk
from nltk.book import *
import re, string

def quita (text):
    return re.sub('[%s]' % re.escape(string.punctuation), '', text)


def leertxt():
    lista = []
    tot = [] 
    num = 0
    archi=open("100mb.txt","r")
    linea=archi.readline()
    while linea!="":
        linea=archi.readline()
        linea2  = quita(linea)
        linea3 = linea2.strip()
        linea4 = linea3.lower() 
        lista = linea4.split(" ")
        for i in range(len(lista)):
            v = lista[i]
            tot.append(v)    
    archi.close()    
    return tot

c = leertxt()
dist1 = FreqDist(c)
x = len(dist1)
y = dist1.most_common(x)
print("\n\tRepetida\n",y)
print(len(y))
