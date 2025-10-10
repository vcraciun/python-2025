"""
Scrieti o functie care converteste un numar din baza 2 in baza 16
Functia va primi ca parametru numarul in baza 2 dar ca valoare numerica in baza 10 (nu sir de caractere si nici reprezentare binara numerica)
Numarul final trebuie sa fie o reprezentare string in baza 16 cu prefixul "0x"
Nu este permisa utilizarea conversiilor din python
"""

def b2tob16(n):
    rez=""
    
    while n>0:
        cif=n%10 * 2**0 + n//10%10 * 2**1 + n//100%10 * 2**2 + n//1000%10 * 2**3
        cif2=0
        for i in range(0, 4):
            cif2+=n//10**i%10*2**i
        n=n//10000
        if(cif>9):
            cifs = chr((cif%10)+ord('A'))
        else:
            cifs = chr(cif)
        rez = cifs + rez
    rez = "0x" + rez
    return rez
     
print(b2tob16(1011))