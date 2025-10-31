#1. calculati al 2000-lea numar fibonacci, stiind ca primele 2 sunt [0, 1]

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, b)
        a, b = b, a + b
    
    return a


print(fibonacci(10))