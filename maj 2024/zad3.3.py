
liczby = []

with open("./Dane/skrot2.txt", "r") as file:
    liczby = file.read().split()


def NWD(a, b):
    while a != b:
        if a > b:
            a = a-b
        else:
            b = b-a
    return a

for liczba in liczby:
    n = int(liczba)
    res = 0
    i = 1

    while n > 0:
        remainder = n % 10
        n = n // 10
        if remainder % 2 == 0:
            pass
        else:
            res += remainder * i
            i *= 10
    nwd = NWD(int(liczba), res)
    if nwd == 7:
        print(liczba)
