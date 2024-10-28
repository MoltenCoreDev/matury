
counter = 0
first_row = []
second_row = []

with open("Dane/liczby_przyklad.txt") as file:
    first_row = file.readline().split()
    second_row = file.readline().split()


for dzielnik in first_row:
    dzielnik = int(dzielnik)
    for dzielna in second_row:
        dzielna = int(dzielna)
        if dzielna % dzielnik == 0:
            print(f"{dzielnik} dzieli sie przez {dzielna}")
            counter += 1
            break
print(counter)