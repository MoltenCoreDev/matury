

def iloczyn(a):
    i = 1
    while a > 0:
        i = i * (a % 10)
        a = a // 10
    return i

for i in range(100, 1000):
    iloczyn(i)

