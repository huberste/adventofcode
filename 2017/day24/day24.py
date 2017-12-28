#!/usr/bin/python3

def getInput(infile):
    result = []
    with open(infile, "r") as inputfile:
        for line in inputfile:
            result.append(list(map(int, line.strip().split("/"))))
    return result

def bridgeStrength(bridge):
    result = 0
    for part in bridge:
        for connector in part:
            result += connector
    return result

def freeConnector(bridge):
    result = 0
    connectors = {}
    for part in bridge:
        for connector in part:
            if connector in connectors:
                connectors[connector] += 1
            else:
                connectors[connector] = 1
    for connector in connectors:
        if (connector != 0) and (connectors[connector] % 2 != 0):
            result = connector
            break
    return result

# recursion to the win!
def strengthenBridge(bridge, parts):
    strongest = bridgeStrength(bridge)
    strongestBridge = bridge
    free = freeConnector(bridge)
    for part in parts:
        if free in part:
            newparts = list(parts)
            newparts.remove(part)
            newbridge = list(bridge)
            newbridge.append(part)
            testbridge = strengthenBridge(newbridge, newparts)
            strength = bridgeStrength(testbridge)
            if strength > strongest:
                strongestBridge = list(testbridge)
                strongest = strength
    return strongestBridge

# recursion to the win!
def prolongBridge(bridge, parts):
    strongest = bridgeStrength(bridge)
    longest = len(bridge)
    longestBridge = bridge
    free = freeConnector(bridge)
    for part in parts:
        if free in part:
            newparts = list(parts)
            newparts.remove(part)
            newbridge = list(bridge)
            newbridge.append(part)
            testbridge = prolongBridge(newbridge, newparts)
            length = len(testbridge)
            if length > longest:
                longestBridge = list(testbridge)
                longest = length
                strongest = bridgeStrength(longestBridge)
            elif length == longest:
                strength = bridgeStrength(testbridge)
                if strength > strongest:
                    longestBridge = list(testbridge)
                    longest = length
                    strongest = strength
    return longestBridge

def main():
    parts= getInput("input")
    # Part 1
    strongest = 0
    strongestBridge = []
    for part in parts:
        if 0 in part:
            newparts = list(parts)
            newparts.remove(part)
            bridge = strengthenBridge([part], newparts)
            strength = bridgeStrength(bridge)
            if strength > strongest:
                strongestBridge = list(bridge)
                strongest = strength
    print("Part 1: Strongest Bridge has strength %d" % strongest)

    # Part :2
    strongest = 0
    longest = 0
    longestBridge = []
    for part in parts:
        if 0 in part:
            newparts = list(parts)
            newparts.remove(part)
            bridge = prolongBridge([part], newparts)
            strength = bridgeStrength(bridge)
            length = len(bridge)
            if length > longest:
                longestBridge = list(bridge)
                longest = length
                strongest = bridgeStrength(longestBridge)
            elif length == longest:
                strength = bridgeStrength(bridge)
                if strength > strongest:
                    longestBridge = list(bridge)
                    longest = length
                    strongest = strength
    print("Part 2: Strongest Longest Bridge has strength %d" % strongest)


if __name__ == "__main__":
    main()
