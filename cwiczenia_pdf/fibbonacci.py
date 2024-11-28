def vfib(n):
    if n == 1 or n == 2:
        return 1
    return vfib(n-2)+vfib(n-1)

def fibonnaci(n):
    if n < 1:
        return []
    fib = []
    for i in range(n):
        if i+1 <= 0:
            continue
        v=vfib(i+1)
        fib.append(v)
    return fib

# f(1) = 1
# f(2) = 1
# f(x) = f(x-2) + f(x-1)

print(fibonnaci(10))
print(fibonnaci(1))
print(fibonnaci(-5))