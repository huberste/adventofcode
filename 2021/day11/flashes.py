#!/usr/bin/env python3

INPUTFILE = "input"
FLASH = 9
RESET = 0
TICKS = 100

def main():
    f = open(INPUTFILE, 'r')
    octopuses = []
    line = f.readline().rstrip()
    while line:
        octopuses.append(list(map(int, list(line))))
        line = f.readline().rstrip()
    f.close()
    flashes = 0
    tick = 0
    while True:
        flashes_before = flashes
        flashed = [[False for col in range(len(octopuses[row]))] for row in range(len(octopuses))]
        # step 1: increase energy of every octopus by 1
        for row in range(len(octopuses)):
            for col in range(len(octopuses[row])):
                octopuses[row][col] += 1
        # step 2: make the flashing happen!
        flash = True
        while flash:
            flash = False
            for row in range(len(octopuses)):
                for col in range(len(octopuses[row])):
                    if (octopuses[row][col] > FLASH) and not flashed[row][col]:
                        flashed[row][col] = True
                        flashes += 1
                        flash = True
                        # check north
                        if row > 0:
                            octopuses[row-1][col] += 1
                        # check east
                        if col < len(octopuses[row]) - 1:
                            octopuses[row][col+1] += 1
                        # check south
                        if row < len(octopuses) - 1:
                            octopuses[row+1][col] += 1
                        # check west
                        if col > 0:
                            octopuses[row][col-1] += 1
                        # check northeast
                        if row > 0 and col < len(octopuses[row]) - 1:
                            octopuses[row-1][col+1] += 1
                        # check southeast
                        if row < len(octopuses) - 1 and col < len(octopuses[row]) - 1:
                            octopuses[row+1][col+1] += 1
                        # check southwest
                        if row < len(octopuses) - 1 and col > 0:
                            octopuses[row+1][col-1] += 1
                        # chech northwest
                        if row > 0 and col > 0:
                            octopuses[row-1][col-1] += 1
        # step 3: reset energy of octopuses
        for row in range(len(octopuses)):
            for col in range(len(octopuses[row])):
                if octopuses[row][col] > FLASH:
                    octopuses[row][col] = RESET
        tick += 1
        if tick == TICKS:
            print("number of flashes after", TICKS, "ticks:",flashes)
        if flashes - flashes_before > 99:
            print("at tick", tick, "all flashes synchronize")
            break

if __name__ == "__main__":
    main()