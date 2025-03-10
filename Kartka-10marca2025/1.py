## 1

# 1.1
from random import random, randint

# n1 = input()
# n2 = input()
#
# print((float(n1)+float(n2))/2)

# 1.2

# n = input()
#
# print(float(n)*float(n))

# 1.3

# print(randint(1, 6))

## 2

# 2.1

# n = input()
#
# if int(n) % 2 == 0:
#     print("parzysta")
# else:
#     print("nieparzysta")

# 2.2

# n = int(input())
#
# if n % 4 == 0:
#     if n % 100 == 0:
#         if n % 400 == 0:
#             print("przestępny")
#         else:
#             print("nie przestepny")
#     else:
#         print("przestępny")
# else:
#     print("nie przestepny")

# 2.3

# a = float(input())
# b = float(input())
#
# if a > 0:
#     print("I cwiartka")
#     if b > 0:
#         print("II Cwiartka")
#     elif b < 0:
#         print("III Cwiartka")
#     print("IV cwiartka")
# elif a < 0:
#     print("II cwiartka")
#     if b > 0:
#         print("I cwiartka")
#     elif b < 0:
#         print("IV cwiartka")
#     print("III cwiartka")
# elif a == 0:
#     if b > 0:
#         print("I cwiartka")
#         print("II cwiartka")
#     elif b < 0:
#         print("III cwiartka")
#         print("IV cwiartka")
#     else:
#         print("OŚ OX")

# 2.4

# procent = float(input())
#
#
# if procent < 0:
#     print("bledne wejscie")
# elif procent <= 50:
#     print(2.0)
# elif procent > 50 and procent <= 60:
#     print(3.0)
# elif procent > 60 and procent <= 70:
#     print(3.5)
# elif procent > 70 and procent <= 80:
#     print(4.0)
# elif procent > 80 and procent <= 90:
#     print(4.5)
# elif procent > 90 and procent <= 100:
#     print(5.0)
# else:
#     print("bledne wejscie")

## 3

# 3.1

# res = 0
#
# for i in range(10):
#     n = int(input("wprowadź liczbe: "))
#     if n % 2 == 0:
#         res += 1
# print(res)

# 3.2

# n = int(input())
#
# res = 0
#
# for i in range(n):
#     res += i
# print(res)

# 3.3

# m = int(input("podaj poczatek zakresu > "))
# n = int(input("podaj koniec zakresu > "))
#
# res = 0
#
# for i in range(m,n):
#
#     if (i+1) % 2 == 1:
#         res += i+1
# print(res)

# 3.4

sum = 0
count = 0

while sum < 100:
    n = int(input("> "))
    count += 1
    sum += n

print(f"Wprowadzono {count} liczb/y")