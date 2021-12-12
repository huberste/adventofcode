#!/usr/bin/env python3

def distance(crabs=[], position=0):
    result = 0
    for crab in crabs:
        result += abs(crab - position)
    return result

def sum_fuel(distance=0):
    return (distance * (distance + 1)) / 2

def crab_distance(crabs=[], position=0):
    result = 0
    for crab in crabs:
        result += int(sum_fuel(abs(crab - position)))
    return result

def main():
    f = open('input', 'r')
    # list of all crabs
    crabs = list(map(int, f.readline().rstrip().split(",")))
    f.close()
    distances = []
    for i in range(min(crabs), max(crabs)+1):
        distances.append(distance(crabs=crabs, position=i))
    print("needed fuel (part 1):", min(distances))

    crab_distances = []
    for i in range(min(crabs), max(crabs)+1):
        crab_distances.append(crab_distance(crabs=crabs, position=i))
    print("needed fuel (part 2):", min(crab_distances))

if __name__ == "__main__":
    main()