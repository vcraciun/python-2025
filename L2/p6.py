"""
Srieti o functie care primeste ca parametru o propozitie si afiseaza pe cate o linie, reprezentarea hex pentru 
codurile ASCII a caracterelor din fiecare cuvant
Practic orice cuvant va fi rescri pe o linie noua, dar in format hex (cate 2 digiti per caracter,
 toti digitii uniti intre ei)
Exemplu, pentru "abc 012" se va afisa
616263
303132   
"""

def fun(s:str):
    for word in s.split():
        p=''
        for c in word:
            p+=hex(ord(c))[2:]
        print(p)

fun('abc 012')