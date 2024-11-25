lista = ["gruszka", "jabłko", "śliwka", "jabłko", "jabłko", "truskawka", "śliwka", "jabłko", "truskawka"]

results = {}

for item in lista:
    if not results.get(item):
        results[item] = 0
    results[item] += 1

print(results)