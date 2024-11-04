from typing import List, Any

counter = 0
first_row: list[Any] = []
second_row = []

with open("Dane/liczby.txt") as file:
    first_row = file.readline().split()
    first_row = [int(e) for e in first_row]
    second_row = file.readline().split()
    second_row = [int(e) for e in second_row]


def sort_arr(arr):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if arr[j] < arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

def prime_factors(n):
    i = 2
    factors = []
    while i <= n:
        if n % i != 0:
            i+= 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

results = []

for liczba in second_row:
    factors = prime_factors(liczba)
    frd = first_row.copy()
    allow = False
    for factor in factors:
        if factor in frd:
            frd.remove(factor)
            allow = True
            #print(f"found factor of {liczba}")
        else:
            allow = False
            break
            #print(f"NOT POSSIBLE FOR {liczba}")
    if allow:
        results.append(str(liczba))

print(" ".join(results))