"""
2.
Generati permutarea 218553019 a cuvantului format din 6 caractere folosind alfabetul "AEGIJLNOPSUVbdefhimnoprstuvwxy". Primul cuvant este "AAAAAA" iar ultimul este "yyyyyy"
Care este cuvantul?
Descrieti 2-3 mecanisme diferite si sortati-le crescator in ordinea performantei pentru a gasi indexul oricarui cuvant dat
"""
a="AEGIJLNOPSUVbdefhimnoprstuvwxy"
k=6
n=218553019

def generate_perms(a, n, k):
    
    char=list(a)
    length=len(char)
    perm=[]

    for i in range(k):
        f=length**(k-i-1)
        index=n//f
        perm.append(char[index])
        n%=f

    return ''.join(perm)

print(generate_perms(a, n, k))
