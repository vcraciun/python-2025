"""
Scrieti o functie care converteste un numar din baza 10 in baza 16
Functia va primi ca parametru numarul in baza 10 si va returna reprezentarea string in baza 16
Numerele convertite in baza 16 vor avea la inceput prefixul "0x"
Nu este permisa utilizarea conversiilor din python
"""


def b10tob16(n):
    result=''
    while(n>0):
        if(n%16 >= 10):
            result = chr(ord('A') + (n%16-10)) + result
        else:
            result = str(n%16) + result
        n=n//16
    return result

print(b10tob16(245))
