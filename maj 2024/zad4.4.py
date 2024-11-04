from typing import List, Any

counter = 0
first_row: list[Any] = []
second_row = []

with open("Dane/liczby.txt") as file:
    first_row = file.readline().split()
    first_row = [int(e) for e in first_row]
    second_row = file.readline().split()
    second_row = [int(e) for e in second_row]

highest_avg = 0
h_c = 0
h_s = 0
f_n = 0

for i in range(len(first_row)):
    if i > len(first_row)-50:
        continue
    sum = 0
    counter = 0
    for j in range(50):
        #print(i+j, end="")
        sum += first_row[i+j]
        counter += 1
    n = 0
    avg = sum / counter
    if avg > highest_avg:
        highest_avg = avg
        h_c = counter
        h_s = sum
        f_n = first_row[i]
    while i+50+n < len(first_row):
        elem = first_row[i+50+n]
        sum += elem
        counter += 1
        avg = sum / counter
        if avg > highest_avg:
            highest_avg = avg
            h_c = counter
            h_s = sum
            f_n = first_row[i]
        n += 1


print(highest_avg,h_c, f_n)