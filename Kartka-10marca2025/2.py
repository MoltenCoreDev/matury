## 5
import math
import random
from random import randint

# 5.1
# arr = []
# s = 0
# for i in range(10):
#     val = int(input("Podaj liczbę \n>"))
#     if val % 2 == 0:
#         s += 1
#     arr.append(val)

# print(arr)
# print(f"jest {s} liczb parzystych")

# 5.2

# arr = []
# s = 1
# for i in range(10):
#     val = int(input("Podaj liczbę \n>"))
#     s *= val
#     arr.append(val)

# print(arr)
# print(f"Iloczyn tych liczb to {s}")

# 5.3
# n = int(input("Ile? \n>"))
# arr = []
# for i in range(n):
#     arr.append(randint(1,50))
#
# sum = 0
# count = 0
#
# print(arr)
#
# for i in arr:
#     if i % 2 == 1:
#         sum += i
#         count += 1
# print(sum/count)

# 5.4
# n = int(input("Ile? \n>"))
# arr = []
# for i in range(n):
#     arr.append(randint(-50,50))
# arr2 = []
# index = 0
# for i in arr:
#     arr2.append(-i)
#     index += 1
# print(arr)
#
# print(arr2)

# 5.5
# n = int(input("Ile? \n>"))
# arr = []
# for i in range(n):
#     arr.append(randint(1,50))
# arr2 = []
# index = 0
# for i in arr:
#     if i < 11 or i > 20:
#         arr2.append(i)
# print(arr)
#
# print(arr2)

#5.6

# arr1 = []
# n = int(input("Ile? \n>"))
# for i in range(n):
#     arr1.append(input("Imie i nazwisko \n>"))
# print("koniec listy pierwszej")
# arr2 = []
# n = int(input("Ile? \n>"))
# for i in range(n):
#     arr2.append(input("Imie i nazwisko \n>"))
# print("koniec listy drugiej")
#
#
# intersection = []
#
# for i in arr1:
#     if i in arr2:
#         intersection.append(i)
#
# union = []
#
# for i in arr1:
#     if i not in union:
#         union.append(i)
#
# for i in arr2:
#     if i not in union:
#         union.append(i)
#
# intersection.sort()
# union.sort()
#
# print(f"część wspólna {intersection}")
# print(f"suma: {union}")
#
#

# 5.7

# n = int(input("Podaj liczbę \n> "))
#
# i = 2
#
# factors = []
#
# while i*i <= n:
#     while n % i == 0:
#         n = n // i
#         factors.append(i)
#     i += 1
# if n > 1:
#     factors.append(n)
#
#
# print(factors)

## 6

# 6.1
#
# n = int(input("Wielkość krawędzi pola \n> "))
#
# xr = int(input("Współrzędna x radaru \n> "))
# yr = int(input("Współrzędna y radaru \n> "))
#
# rr = int(input("Zasięg radaru \n> "))
#
# field = []
#
# for i in range(n):
#     field.append([])
#     for j in range(n):
#         field[i].append(random.randrange(0,9))
#
# results = []
#
# for x in range(len(field)):
#     for y in range(len(field[x])):
#         dist = math.sqrt(abs(xr-x) + abs(yr-y))
#         if dist < rr:
#             results.append(f"x: {x}, y: {y}, value: {field[x][y]}")
#
# print("\n".join(results))

# 6.2 i 6.3

class Tree:
    def __init__(self, gatunek, wysokosc, srednica):
        self.gatunek = gatunek
        self.wysokosc = wysokosc
        self.srednica = srednica

trees = [Tree("sosna", 2.01, 35.00),
         Tree("brzoza", 1.98, 29.50),
         Tree("klon", 2.50, 31.02),
         Tree("sosna", 2.12, 37.50),
         Tree("modrzew", 1.45, 19.56),
         Tree("dab", 2.35, 50.00),
         Tree("swierk", 2.24, 42.01),
         Tree("klon", 1.53, 25.25)]

highest_tree_index = 0
highest_tree_height = trees[0].wysokosc

for i in range(len(trees)):
    h = trees[i].wysokosc
    if highest_tree_height < h:
        highest_tree_height = h
        highest_tree_index = i

print(trees[i].gatunek)
