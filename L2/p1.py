"""
Scrieti o functie care converteste un numar din baza 10 in baza 2
Functia va primi ca parametru numarul in baza 10 si va returna reprezentarea string in baza 2
Numerele convertite in baza 2 vor avea la inceput prefixul "0b"
Nu este permisa utilizarea conversiilor din python
"""

def base2_conversion(number):
    b2_number = "0b"
    while(number > 0):
        b2_number += str(number%2)
        number //= 2
    return b2_number

print(base2_conversion(234))
print(0b01010111)
