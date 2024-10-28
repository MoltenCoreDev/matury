
counter = 0
first_row = []
second_row = []

with open("Dane/liczby_przyklad.txt") as file:
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
    while i*i <= n:
        if n % i:
            i+= 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


for liczba in second_row:

