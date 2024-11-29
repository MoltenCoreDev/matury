data = ""

with open("Dane/BIT18.txt") as file:
    data = file.read()


data = data.split("\n")
data = [packet.split(" ") for packet in data]
data = [[int(packet[0]), int(packet[1])] for packet in data]

rdata = list(reversed(data))

longest_column = 0
column_size = 0

counter = 0
p_speed = rdata[0][1]
for line in rdata:
    speed = line[1]
    if speed > p_speed:
        counter += 1
        if column_size > longest_column:
            longest_column = column_size
        column_size = 1
    else:
        column_size += 1
    p_speed = speed

print(longest_column)

print(rdata)