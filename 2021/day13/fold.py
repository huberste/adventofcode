#!/usr/bin/env python3

INPUTFILE = "input"
X = 0
Y = 1

def main():
    f = open(INPUTFILE, 'r')
    points = []
    folds = []
    line = f.readline().rstrip()
    while line:
        points.append(list(map(int, line.split(","))))
        line = f.readline().rstrip()
    line = f.readline().rstrip()
    while line:
        fold = line.split("fold along ")[1]
        fold = fold.split("=")
        fold[1] = int(fold[1])
        folds.append(fold)
        line = f.readline().rstrip()
    f.close()
    loop = 0
    for fold in folds:
        for point in points:
            if fold[0] == "x":
                if point[X] > fold[1]:
                    point[X] = fold[1] - (point[X] - fold[1])
            if fold[0] == "y":
                if point[Y] > fold[1]:
                    point[Y] = fold[1] - (point[Y] - fold[1])
        i = 0
        while i < len(points):
            j = i + 1
            while j < len(points):
                if points[i][X] == points[j][X] and points[i][Y] == points[j][Y]:
                    points.pop(j)
                    j -= 1
                j += 1
            i += 1
        loop += 1
        if loop == 1:
            print("Number of points after the first fold:", len(points))
    
    print("Part 2: Number of points after last fold:", len(points))
    for y in range(-1,7):
        for x in range(-1,40):
            symbol = "."
            for point in points:
                if point[X] == x and point[Y] == y:
                    symbol = "X"
            print(symbol, end="")
        print()

if __name__ == "__main__":
    main()