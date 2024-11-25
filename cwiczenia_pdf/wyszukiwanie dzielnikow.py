
res = []
def dzielniki(liczba):
    n = 1
    num = liczba
    while n*n <= liczba:
        if num % n == 0:
            res.append(n)
            num = num//n
        n += 1

dzielniki(10)

print(res)
