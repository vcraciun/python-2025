def tokenize(expr):
    tokens=[]
    current=""

    for ch in expr:
        if str.isdigit(ch):
            current += ch
        else:
            if(current):
                tokens.append(current)
                current=""
            tokens.append(ch)
    return tokens

def eval_expression(expr: str)-> int:

    calc={
        "+": lambda a, b: int(a)+int(b),
        "-": lambda a, b: int(a)-int(b),
        "*": lambda a, b: int(a)*int(b),
        "/": lambda a, b: int(a)//int(b)
    }

    lista=[]

    t = tokenize(expr)

    for i in range (0, len(t)-1):
        if t[i] in ["*","/"]:
            a = lista.pop()
            b = t[i+1]
            res = calc[t[i]](a,b)
            print(a,b,t[i],res)
            lista.append(res)
        else:
            lista.append(t[i])

    result = lista[0]

    for i in range(0,len(lista)-1):
        if lista[i] in ["+", "-"]:
            a = result
            b = lista[i+1]
            result = calc[lista[i]](a,b)
            print(a,b,lista[i], result)

    return result

print(eval_expression("4+17-9/2+4"))



