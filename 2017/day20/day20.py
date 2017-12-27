#!/usr/bin/python3

import sys
import math

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

def collision(particle1, particle2):
    result = (-1, -1, -1)
    # check x axis
    pos1, vel1, acc1 = particle1
    pos2, vel2, acc2 = particle2
    v_1 = vel1[0]
    v_2 = vel2[0]
    a_1 = acc1[0]
    a_2 = acc2[0]
    x_1 = pos1[0]
    x_2 = pos2[0]
    tx_1 = -(v_1 - v_2) + math.sqrt((v_1 - v_2)**2 - 4 * (1/2*(a_1 - a_2)) * x_1 - x_2) / 2 (1/2 * (a_1 - a_2))
    tx_2 = -(v_1 - v_2) - math.sqrt((v_1 - v_2)**2 - 4 * (1/2*(a_1 - a_2)) * x_1 - x_2) / 2 (1/2 * (a_1 - a_2))
    if tx_1 % 1 == 0:
        if tx_1 > 0:
            # check second axis
            v_1 = vel1[1]
            v_2 = vel2[1]
            a_1 = acc1[1]
            a_2 = acc2[1]
            x_1 = pos1[1]
            x_2 = pos2[1]
            ty_1 = -(v_1 - v_2) + math.sqrt((v_1 - v_2)**2 - 4 * (1/2*(a_1 - a_2)) * x_1 - x_2) / 2 (1/2 * (a_1 - a_2))
            ty_2 = -(v_1 - v_2) - math.sqrt((v_1 - v_2)**2 - 4 * (1/2*(a_1 - a_2)) * x_1 - x_2) / 2 (1/2 * (a_1 - a_2))
            
    if tx_2 % 1 == 0:
        if tx_2 > 0:
           #todo 
           return result
    return result

def main(args):
    inputfile = ""
    if len(args) > 1:
        inputfile = args[1]
    else:
        inputfile = "input"
    particles = getInput(inputfile)
    # part1
    nearest = -1
    nearestDistance = float("inf")
    TIME = 1000
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
    print("Part1: nearest particle: %d" % nearest)

    for tick in range(TIME):
        # check for collisions
        collided = []
        for i in range(len(particles)):
            for j in range(i+1, len(particles)):
                if ((particles[i][0][0] == particles[j][0][0]) and
                    (particles[i][0][1] == particles[j][0][1]) and
                    (particles[i][0][2] == particles[j][0][2])):
                    if not i in collided:
                        collided.append(i)
                    if not j in collided:
                        collided.append(j)
        collided = list(reversed(sorted(collided)))
        for particle in collided:
            particles.pop(particle)
        # move particles
        for i in range(len(particles)):
            pos, vel, acc = particles[i]
            for dim in range(3):
                vel[dim] = vel[dim] + acc[dim]
                pos[dim] = pos[dim] + vel[dim]
            particles[i] = (pos, vel, acc)
    print("Part2: particles left: %d" % len(particles))

"""
    # part2
    destroyed = []
    for i in range(len(particles)):
        destroyed.append(False)

    # list all collisions
    # sort collisions by time
    # work on collisions (if both particles still exist)
    collisions = []
    # one collision is (particle1, particle2, time)
    for i in range(len(particles)):
        particle1 = particles[i]
        for j in range(i+1, len(particles)):
            particle2 = particles[j]
        # math: 1/2 * a t^2 + v_0 * t + x_0
        # collision: 1/2 a_1 * t^2 + v_1 * t + x_1 = 1/2 a_2 * t^2 + v_2 * t + x_2
        # 0 = (1/2 * a_1 - 1/2 * a_2) * t^2 + (v_1 - v_2) * t + (x_1 - x_2)
        # t_1,2 = -(v_1 - v_2) +/- sqrt((v_1 - v_2)^2 - 4 * (1/2*(a_1 - a_2)) * x_1 - x_2) / 2 (1/2 * (a_1 - a_2))
"""
if __name__ == "__main__":
    main(sys.argv)
