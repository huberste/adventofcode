#!/usr/bin/python3

import sys

def getInput(inputfile):
    result = []
    with open(inputfile, 'r') as infile:
        for line in infile:
            splitline = line.strip().split(", ")
            pos = splitline[0][3:-1].split(",")
            vel = splitline[1][3:-1].split(",")
            acc = splitline[2][3:-1].split(",")
            for i in range(3):
                pos[i] = int(pos[i])
                vel[i] = int(vel[i])
                acc[i] = int(acc[i])
            result.append((pos, vel, acc))
    return result

def dist(t, acc, vel, pos):
    return (0.5 * acc * t * t + vel * t + pos)

def main(args):
    inputfile = ""
    if len(args) > 1:
        inputfile = args[1]
    else:
        inputfile = "input"
    particles = getInput(inputfile)
    nearest = -1
    nearestDistance = float("inf")
    TIME = 100000
    for i in range(len(particles)):
        particle = particles[i]
        pos, vel, acc = particle
        x = dist(TIME, acc[0], vel[0], pos[0])
        y = dist(TIME, acc[1], vel[1], pos[1])
        z = dist(TIME, acc[2], vel[2], pos[2])
        distance = abs(x) + abs(y) + abs(z)
        if distance < nearestDistance:
            nearestDistance = distance
            nearest = i

    print(nearest, nearestDistance)

if __name__ == "__main__":
    main(sys.argv)
