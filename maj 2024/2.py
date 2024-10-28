
n = 39101

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
    print("remainder", remainder)
print(res)