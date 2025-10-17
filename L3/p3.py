"""
afisati continutul unui text, in format hexazecimal pe un tabel cu 17 coloane
prima coloana va contine indexul hex pe 4 digiti pentru valoarea imediat urmatoare
celelalte coloane vor contine cate 1 element hex reprezentat pe 2 digiti, aliniat dreapta si umplut cu 0
prima linie este de asemenea un header cu indexii elementelor de pe fiecare linie (00-0F)

Exemplu:
       00 01 02 03 04 05 06 07 08 09 0A 0B 0C 0D 0E 0F
     +------------------------------------------------
0000 | 05 46 9A 5D FF FF 00 00 00 11 19 18 43 44 59 A6 
0010 | 3D 44 77 78 FF FF FF 00 00 00 00 00 00 00 00 00 
0020 | 10 10 1D 3B 5A 64
"""

mesaj = "1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

my_list = []

for i in mesaj:
    c = hex(ord(i))[2:].upper() 

    my_list.append(c)

rows = len(my_list)//16
last_row = len(my_list)%16

for i in range(len(my_list)):
    if i % 16 == 0 and i > 0:
        print("")
    print(my_list[i],end = " ",flush = True)
    



