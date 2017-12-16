#!/usr/bin/python3

def getInput(inputfile):
    result = []
    with open(inputfile, 'r') as infile:
        for line in infile:
            splitline = line.strip().split(",")
            for move in splitline:
                result.append(move)
    return result

def processMove(dancefloor, move):
    if move[0] == "s":
        # spin
        for i in range(int(move[1:])):
            element = dancefloor.pop()
            dancefloor.insert(0, element)
    elif move[0] == "x":
        # exchange
        positions = move[1:].split("/")
        a = int(positions[0])
        b = int(positions[1])
        element = dancefloor[a]
        dancefloor[a] = dancefloor[b]
        dancefloor[b] = element
    elif move[0] == "p":
        a = dancefloor.index(move[1])
        b = dancefloor.index(move[3])
        element = dancefloor[a]
        dancefloor[a] = dancefloor[b]
        dancefloor[b] = element
    return dancefloor

def main():
    moves = getInput("input")
    # programs a..p = 0..15
    order = "abcdefghijklmnop"
    dancefloor = list(order)
    seen = [order]
    stilltodo = 0
    repetitions = 1000000000
    for i in range(repetitions):
        for move in moves:
            dancefloor = processMove(dancefloor, move)
        order = ''.join(dancefloor)
        if not (order in seen):
            seen.append(order)
        else:
            cycle = i - seen.index(order) + 1
            stilltodo = repetitions % cycle
            print("Order of the programs after one billion dances: %s" % seen[stilltodo])
            break
        if i == 0:
            print("Order of the programs after the first dance: %s" % order)

if __name__ == "__main__":
    main()
