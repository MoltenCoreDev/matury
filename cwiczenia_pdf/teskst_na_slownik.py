tekst = "login=user;password=pass;port=5432;database=name"

pairs = tekst.split(";")

results = {}

for pair in pairs:
    i = pair.split("=")
    key = i[0]
    value = i[1]
    results[key] = value

print(results)