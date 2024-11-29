import json

lista = [
{ "x": 0, "y":0.5, "opis": "punkt 1" },
{ "x": 1.3, "y":2, "opis": "punkt 2" },
{ "x": 1.1, "y":1.5, "opis": "punkt 3" },
]


def to_csv(obj):
    res = ""
    # create index
    row = []
    for key in obj[0].keys():
        row.append(key)
    res += ",".join(row) + "\n"
    for line in obj:
        row = []
        for val in line.values():
            row.append(val)
        row = [str(elem) for elem in row]
        res += ",".join(row) + "\n"


    return res

with open("data/punkty.csv", "w+") as file:
    file.write(to_csv(lista))