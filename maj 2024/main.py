from decimal import Decimal

b = 1
c = Decimal(0)
n = 333333666666999999

counter = 0

while n>0:
    a = n % 10
    n = n // 10
    if a % 2 == 0:
        c = c + b*Decimal(a/2)
    else:
        c = Decimal(c + b)
        counter += 1
    b = b*10

print(c)
print("counter: ", counter)