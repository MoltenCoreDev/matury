from math import sqrt

with open("data/linia.csv", "r") as file:
    points = file.read()
    points = points.split("\n")
    points = [point.split(",") for point in points]
    points = [[float(point[0]), float(point[1])] for point in points]

tl = 0

def length(point1, point2):
    xl = abs(point1[0] - point2[0])
    yl = abs(point1[1] - point2[1])
    return sqrt(xl*xl + yl*yl)


for i in range(len(points)):
    if i == 0:
        continue
    sl = length(points[i-1], points[i])
    tl += sl


print(tl)