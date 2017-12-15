#!/usr/bin/python3

def getInput(inputfile):
    result = {}
    with open(inputfile, 'r') as infile:
        for line in infile:
            splitline = line.strip().split(": ")
            dpth = int(splitline[0])
            rnge = int(splitline[1])
            result[dpth] = rnge
    return result

def position(rnge, picosecond):
    result = picosecond % (2*(rnge-1))
    if result > rnge-1:
        result = (rnge-1) - (result - (rnge-1))
    return result

def severity(layers, wait):
    result = 0
    maxdepth = 0
    maxrange = 0
    for depth in layers:
        if depth > maxdepth:
            maxdepth = depth
        if layers[depth] > maxrange:
            maxrange = layers[depth]
    for picosecond in range(maxdepth+1):
        if picosecond in layers:
            if position(layers[picosecond], picosecond + wait) == 0:
                result = result + (picosecond * layers[picosecond])
    return result

def caught(layers, wait):
    result = False
    maxdepth = 0
    maxrange = 0
    for depth in layers:
        if depth > maxdepth:
            maxdepth = depth
        if layers[depth] > maxrange:
            maxrange = layers[depth]
    for picosecond in range(maxdepth+1):
        if picosecond in layers:
            if position(layers[picosecond], picosecond + wait) == 0:
                result = True
                break
    return result

def printState(layers, picosecond):
    line = "  "
    maxdepth = 0
    maxrange = 0
    for depth in layers:
        if depth > maxdepth:
            maxdepth = depth
        if layers[depth] > maxrange:
            maxrange = layers[depth]
    print("maxdepth: %d" % maxdepth)
    print("maxrange: %d" % maxrange)
    # print layer numbers
    for i in range(maxdepth + 1):
        line = line + "%2d  " % i
    print(line)

    for i in range(maxrange):
        line = ""
        line = line + "%2d" % i
        for depth in range(maxdepth + 1):
            if depth in layers:
                if i < layers[depth]:
                    line = line + "["
                    if position(layers[depth], picosecond) == i:
                        line = line + "X"
                    else:
                        line = line + " "
                    line = line + "] "
                else:
                    line = line + "    "
            else:
                line = line + "    "
        print(line)

def main():
    layers = getInput("input")
    print("Severity: %d" % severity(layers, 0))
    wait = 0
    while caught(layers, wait):
        wait = wait + 1
    print("I need to wait for %d picoseconds so I won't get caught." %wait)
    
if __name__ == "__main__":
    main()
