
def dzielniki(liczba):
    res = []
    n = 1
    while n < liczba:
        if liczba % n == 0:
            res.append(n)
        n += 1
    return res

print(dzielniki(10))
