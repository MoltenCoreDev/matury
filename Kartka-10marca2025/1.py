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

# sum = 0
# count = 0

# while sum < 100:
#     n = int(input("> "))
#     count += 1
#     sum += n
#
# print(f"Wprowadzono {count} liczb/y")

# 3.5

# haslo = "haslo"
# def zaloguj():
#     for i in range(3):
#         inp = input(f"Wprowadź hasło... pozostało: {3-i} prób.\n> ")
#         if inp == haslo:
#             print("Zalogowano")
#             return True
#         else:
#             print("Błędne hasło")
#     print("Nie możesz się teraz zalogować.")
# zaloguj()

# 3.6

# print("Gra zgadywanka")
# l = int(input("Podaj najmniejszą liczbe całkowitą do losowania\n>"))
# m = int(input("Podaj największą liczbe całkowitą do losowania\n>"))
#
# num = randint(l,m)
# while True:
#     guess = int(input("Podaj swój strzał\n>"))
#     if guess < num:
#         print("za mało!")
#     elif num == guess:
#         print("Brawo zgadłxś!")
#         break
#     else:
#         print("za duzo!")

# 3.7

# podzielne = [x for x in range(0,100,3)]
#
# n = input("Ile liczb losowych podzielnych przez 3? \n>")
#
# for i in range(int(n)):
#     print(podzielne[randint(0,len(podzielne))])

# 3.8

# def czy_pierwsza(n: int):
#     i = 1
#     pf = []
#     while i*i <= n:
#         if n % i == 0:
#             pf.append(i)
#             n = n // i
#         i+=1
#         if len(pf) > 2:
#             break
#     return len(pf) < 2
#
# print(czy_pierwsza(int(input("Liczba do sprawdzenia \n>"))))

# 3.9

# num = input("liczba \n>")
# sum = 0
#
# for letter in num:
#     n = int(letter)
#     sum += n
#
# print(sum)

# 4.1
#
# napis = input("napis \n>")
#
# print(len(napis))

# 4.2

# napis1 = input("napis1\n>")
# napis2 = input("napis2\n>")
#
# if napis2 in napis1:
#     print("Pierwszy substring",napis1.find(napis2))
#     print("Ilość: ", napis1.count(napis2))
#     print("Ostatni substring", napis1.rfind(napis2))

# 4.3

# napis = input("Napis \n>")
#
# if len(napis) < 2:
#     print("Napis za krótki :(")
#
# print(napis[0], napis[1], napis[2:])
#
# print(napis[-1], napis[-2], napis[:-2])
#
# print([napis[n] for n in range(0, len(napis), 2)])
# print([napis[-n] for n in range(1, len(napis), 2)])

# 4.4

# napis = input("Napis\n>")
#
# if napis == napis[::-1]:
#     print(f"{napis} jest palindromem!")
# else:
#     print(f"{napis} nie jest palindromem!")

# 4.5

# num = input("liczba \n>")
# sum = 0
#
# for letter in num:
#     n = int(letter)
#     sum += n
#
# print(sum)

# 4.6

dlugosc = input("podaj długość \n>")

def generuj_znak():
    znaki = "ABCDEFGHIJKLMNOPQRSTUVWXYZ123456789*&^%$#@!"
    return znaki[randint(0, len(znaki)-1)]