

def iloczyn(a):
    i = 1
    while a > 0:
        i = i * (a % 10)
        a = a // 10
    return i

def prime_factors(n):
    i = 1
    res = []
    while i <= n:
        if n % i == 0:
            res.append(i)
            n = n//i

        i+= 1
    return res

print(prime_factors(18))