#!/usr/bin/env python3

f = open('input', 'r')
lines = []
line = f.readline()
maxx = 0
maxy = 0
while line:
    coords = line.rstrip().split(" -> ")
    temp = [list(map(int, coords[0].split(","))), list(map(int, coords[1].split(",")))]
    lines.append(temp)
    for point in temp:
        if point[0] > maxx:
            maxx = point[0]
        if point[1] > maxy:
            maxy = point[1]
    line = f.readline()

X = 0
Y = 1
area = [[0 for x in range(maxy+1)] for y in range(maxx+1)]
for line in lines:
    # consider only horizontal and vertical lines
    if line[0][X] == line[1][X]: # same x: vertical
        for y in range(min(line[0][Y], line[1][Y]), max(line[0][Y], line[1][Y]) + 1):
            area[line[0][X]][y] += 1
    if line[0][Y] == line[1][Y]: # same y: horizontal
        for x in range(min(line[0][X], line[1][X]), max(line[0][X], line[1][X]) + 1):
            area[x][line[0][Y]] += 1

count = 0
for x in range(maxx+1):
    for y in range(maxy+1):
        if area[x][y] > 1:
            count +=1
print("Only horizontal and vertical lines:", count)

x = 0
y = 0
for line in lines:
    # diagonal lines only
    if (line[0][X] != line[1][X]) and (line[0][Y] != line[1][Y]):
        x = line[0][X]
        y = line[0][Y]
        stepx = 1
        if line[0][X] > line[1][X]:
            stepx = -1
        stepy = 1
        if line[0][Y] > line[1][Y]:
            stepy = -1
        while x != line[1][X]:
            area[x][y] += 1
            x += stepx
            y += stepy
        area[x][y] += 1

count = 0
for x in range(maxx+1):
    for y in range(maxy+1):
        if area[x][y] > 1:
            count +=1
print("All lines:", count)