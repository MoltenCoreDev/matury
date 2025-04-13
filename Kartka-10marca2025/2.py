## 5
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

arr1 = []
n = int(input("Ile? \n>"))
for i in range(n):
    arr1.append(input("Imie i nazwisko \n>"))
print("koniec listy pierwszej")
arr2 = []
n = int(input("Ile? \n>"))
for i in range(n):
    arr2.append(input("Imie i nazwisko \n>"))
print("koniec listy drugiej")


intersection = []

for i in arr1:
    if i in arr2:
        intersection.append(i)

union = []

for i in arr1:
    if i not in union:
        union.append(i)

for i in arr2:
    if i not in union:
        union.append(i)

print(f"część wspólna {intersection}")
print(f"suma: {union}")

