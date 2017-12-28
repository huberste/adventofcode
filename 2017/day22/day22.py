#!/usr/bin/python3

def getInput(inputfile):
    virusmap = {}
    lines = []
    with open(inputfile, 'r') as infile:
        for line in infile:
            lines.append(line.strip())
    midx = (len(lines[0]) + 1) / 2
    midy = (len(lines) + 1) / 2
    for i in range(len(lines)):
        y = i - (midy - 1)
        for j in range(len(lines[i])):
            x = j - (midx - 1)
            if (lines[i][j]) == "#":
                virusmap[(x,y)] = "#"
            else:
                virusmap[(x,y)] = "."
    return virusmap

def main():
    # Part 1
    virusmap = getInput("input")
    x = 0
    y = 0
    counter = 0
    direction = 0 # 0N1E2S3W
    for burst in range(10000):
        if (x,y) in virusmap:
            if virusmap[(x,y)] == "#":
                #print("%d,%d is infected. turning right and desinfecting."% (x,y))
                direction = (direction + 1) % 4 # turn right
                virusmap[(x,y)] = "."
            else:
                #print("%d,%d is not infected. turning left and infecting."% (x,y))
                direction = (direction - 1) % 4 # turn left
                virusmap[(x,y)] = "#"
                counter += 1
        else:
            #print("%d,%d is not infected. turning left and infecting."% (x,y))
            direction = (direction - 1) % 4 # turn left
            virusmap[(x,y)] = "#"
            counter += 1
        if direction == 0: # N
            y = y - 1
        elif direction == 1: # E
            x = x + 1
        elif direction == 2: # S
            y = y + 1
        elif direction == 3: # W
            x = x - 1

    print("part1: Bursts with infection: %d" % counter)

    # Part 2
    virusmap = getInput("input")
    x = 0
    y = 0
    counter = 0
    direction = 0 # 0N1E2S3W
    for burst in range(10000000):
        if (x,y) in virusmap:
            if virusmap[(x,y)] == "#":
                #print("%d,%d is infected. turning right and flagging."% (x,y))
                direction = (direction + 1) % 4 # turn right
                virusmap[(x,y)] = "F"
            elif virusmap[(x,y)] == "W":
                #print("%d,%d is W. Infecting."% (x,y))
                counter += 1
                virusmap[(x,y)] = "#"
            elif virusmap[(x,y)] == "F":
                #print("%d,%d is F. Reversing and desinfecting."% (x,y))
                direction = (direction + 2) % 4 # reverse
                virusmap[(x,y)] = "."
            elif virusmap[(x,y)] == ".":
                #print("%d,%d is not infected. turning left and weakening."% (x,y))
                direction = (direction - 1) % 4 # turn left
                virusmap[(x,y)] = "W"
        else:
            #print("%d,%d is not infected. Turning left and weakening."% (x,y))
            direction = (direction - 1) % 4 # turn left
            virusmap[(x,y)] = "W"
        if direction == 0: # N
            y = y - 1
        elif direction == 1: # E
            x = x + 1
        elif direction == 2: # S
            y = y + 1
        elif direction == 3: # W
            x = x - 1

    print("part1: Bursts with infection: %d" % counter)

if __name__ == "__main__":
    main()
