#!/usr/bin/python3

def getInput(infile):
    result = []
    with open(infile, "r") as inputfile:
        for line in inputfile:
            result.append(list(map(int, line.strip().split("/"))))
    return result

BEGIN_STATE = "A"
CHECKSUM_AFTER = 12994925

def main():
    tape = {}
    state = BEGIN_STATE
    pos = 0
    for step in range(CHECKSUM_AFTER):
        value = 0
        if pos in tape:
            value = tape[pos]
        else:
            tape[pos] = value
        if state == "A":
            if value == 0:
                tape[pos] = 1
                pos += 1 # move right
                state = "B"
            else: # value = 1
                tape[pos] = 0
                pos -= 1 # move left
                state = "F"
        elif state == "B":
            if value == 0:
                tape[pos] = 0
                pos += 1 # move right
                state = "C"
            else: # value = 1
                tape[pos] = 0
                pos += 1 # move left
                state = "D"
        elif state == "C":
            if value == 0:
                tape[pos] = 1
                pos -= 1 # move right
                state = "D"
            else: # value = 1
                tape[pos] = 1
                pos += 1 # move left
                state = "E"
        elif state == "D":
            if value == 0:
                tape[pos] = 0
                pos -= 1 # move right
                state = "E"
            else: # value = 1
                tape[pos] = 0
                pos -= 1 # move left
                state = "D"
        elif state == "E":
            if value == 0:
                tape[pos] = 0
                pos += 1 # move right
                state = "A"
            else: # value = 1
                tape[pos] = 1
                pos += 1 # move left
                state = "C"
        elif state == "F":
            if value == 0:
                tape[pos] = 1
                pos -= 1 # move right
                state = "A"
            else: # value = 1
                tape[pos] = 1
                pos += 1 # move left
                state = "A"

    checksum = 0
    for place in tape:
        if tape[place] == 1:
            checksum += 1
    print("Part 1: Diagnostic Checksum = %d" % checksum)

if __name__ == "__main__":
    main()
