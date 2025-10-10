"""
Srieti o functie care primeste ca parametru o expreise matematica cu paranteze rotunde si verifica daca parantezarea este sau nu corecta
Exemplu 1: "6+8*(5+3/2-1+6/(3+9)-7*(5+7/3))" va returna True
Exemplu 2: "8-4*(3+7/8+4/(5-9)" va returna False
"""

def check_parantheses(expr):
    count = 0
    for ch in expr:
        if ch == '(':
            count += 1
        elif ch == ')':
            if count == 0:
                return False
            count -= 1
    return count == 0

print(check_parantheses("6+8*(5+3/2-1+6/(3+9)-7*(5+7/3))"))
print(check_parantheses("8-4*(3+7/8+4/(5-9)"))