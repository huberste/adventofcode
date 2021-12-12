#!/usr/bin/env python3

INPUTFILE = "input"

def extend_basin(basin, area):
    for point in basin:
        x = point[0]
        y = point[1]
        # check north
        if y > 0:
            if area[y-1][x] <9:
                if not [x, y-1] in basin:
                    basin.append([x, y-1])
        # check east
        if x < len(area[y]) - 1:
            if area[y][x+1] < 9:
                if not [x+1, y] in basin:
                    basin.append([x+1, y])
        # check south
        if y < len(area) - 1:
            if area[y+1][x] < 9:
                if not [x, y+1] in basin:
                    basin.append([x, y+1])
        # check west
        if x > 0:
            if area[y][x-1] < 9:
                if not [x-1, y] in basin:
                    basin.append([x-1, y])
    return basin

def main():
    f = open(INPUTFILE, 'r')
    area = []
    line = f.readline().rstrip()
    while line:
        area.append(list(map(int, list(line))))
        line = f.readline().rstrip()
    f.close()

    low_points = []
    for y in range(len(area)):
        for x in range(len(area[y])):
            # check north
            if y > 0:
                if area[y-1][x] <= area[y][x]:
                    continue
            # check east
            if x < len(area[y]) - 1:
                if area[y][x+1] <= area[y][x]:
                    continue
            # check south
            if y < len(area) - 1:
                if area[y+1][x] <= area[y][x]:
                    continue
            # check west
            if x > 0:
                if area[y][x-1] <= area[y][x]:
                    continue
            low_points.append([x, y])

    risk = 0
    for point in low_points:
        risk += 1 + area[point[1]][point[0]]
    print("risk", risk)

    basins = []
    for point in low_points:
        basins.append([point])
    for i in range(len(basins)):
        basins[i] = extend_basin(basins[i], area)
    sizes = [len(basin) for basin in basins]
    sizes.sort()
    sum = 1
    for size in sizes[-3:]:
        sum *= size
    print(sum)


if __name__ == "__main__":
    main()