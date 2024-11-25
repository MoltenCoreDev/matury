lista = [2,7,3,5,1,6]

res = []
for number in range(10):
    if number not in lista:
        res.append(number)
print(res)