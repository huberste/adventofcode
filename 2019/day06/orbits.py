#! /usr/bin/env python3

INPUTFILE = 'input'

SANTA = "SAN"
YOU = "YOU"

"""
orbiting():
counts all (direct and indirect) orbits for one "center" object
"""
def orbiting(orbits, center):
    result = 0
    if center in orbits:
        for satellite in orbits[center]:
            result += orbiting(orbits, satellite) # all orbiting of satellite
            result += 1 # count all directly orbiting
            print("   [DEBUG] satellite:", satellite, "orbits:", result)
        #result += len(orbits[center])
    print("[DEBUG] center:", center, "orbits:", result)
    return result

def calculate_orbits(orbiting_around):
    result = 0
    for satellite in orbiting_around:
        sat = satellite
        while sat:
            if sat in orbiting_around:
                sat = orbiting_around[sat]
                result += 1
            else:
                sat = 0
    return result

def search_center(orbiting_around, center, object_one):
    if object_one in orbiting_around:
        parent = orbiting_around[object_one]
        print("parent:", parent, "center:", center)
        if parent == center:
            return 0
        else:
            path_to_center = search_center(orbiting_around, center, parent)
            if path_to_center < 0:
                return -1
            else:
                return path_to_center + 1
    else:
        return -1

def calculate_transfers(orbits, orbiting_around, object_one, object_two):
    result = -1
    parent = object_one
    min_steps = 9999999
    while parent in orbiting_around:
        result += 1
        parent = orbiting_around[parent]
        steps = search_center(orbiting_around, parent, object_two)
        print("<", parent, result, steps)

        if steps < 0:
            steps = 9999999
        if min_steps > (result + steps):
            min_steps = result + steps
    return min_steps

def main():
    orbits = {}
    orbiting_around = {}
    # read Universal Orbit Map from input file
    input_file = open(INPUTFILE, 'r')
    line = input_file.readline().strip()
    while line:
        center, orbit = line.split(")")
        if center in orbits:
            orbits[center].append(orbit)
        else:
            orbits[center] = []
            orbits[center].append(orbit)
        orbiting_around[orbit] = center
        line = input_file.readline().strip()
    input_file.close()

    # Part 1
    print("total orbits:", calculate_orbits(orbiting_around))

    # Part 2 Distance between YOU and SAN
    print("Transfers from YOU to SAN:", calculate_transfers(orbits, orbiting_around, YOU, SANTA))

if __name__ == "__main__":
    main()
