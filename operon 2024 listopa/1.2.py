data = ""

with open("Dane/BIT18.txt") as file:
    data = file.read()


data = data.split("\n")
data = [packet.split(" ") for packet in data]
data = [[int(packet[0]), int(packet[1])] for packet in data]

rdata = list(reversed(data))

columns = []

counter = 0
p_speed = rdata[0][1]
current_column = []
for line in rdata:
    speed = line[1]

    if speed > p_speed:
        columns.append(current_column)
        current_column = [speed]
        # print("nowa kolumna")
    else:
        current_column.append(speed)
        #print("dodawanie do kolumny")

    p_speed = speed

res = []


for column in columns:
    maxi = max(column)
    mini = min(column)
    res.append(abs(maxi-mini))

print(max(res))