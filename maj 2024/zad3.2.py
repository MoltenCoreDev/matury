
counter = 0
biggest_empty = 0
liczby = []

with open("./Dane/skrot.txt", "r") as file:
    liczby = file.read().split()

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
    if res == 0:
        if int(liczba) > biggest_empty:
            biggest_empty = int(liczba)
        counter += 1
    #print(f"{liczba} wyniki: {res}")
print(counter)
print(biggest_empty)