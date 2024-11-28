import json

lista = [
{ "x": 0, "y":0.5, "opis": "punkt 1" },
{ "x": 1.3, "y":2, "opis": "punkt 2" },
{ "x": 1.1, "y":1.5, "opis": "punkt 3" },
]


def to_csv(obj):
    res = ""
    # create index
    for key in obj[0].keys():
        res += f"{key}"
        res += ","
    res += "\n"

    
    return res

print(to_csv(lista))

with open("data/punkty.csv", "w+") as file:
    pass