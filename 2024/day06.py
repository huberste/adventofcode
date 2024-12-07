#! /usr/bin/env python3
"""Module for solving advent of code 2024/06"""

import copy

INPUT = "day06.input"

UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

OBSTACLE = "#"
GUARD = "^"
VISITED = "X"

def rotate(direction):
    """rotate the direction by 90° clockwise"""
    if direction == UP:
        return RIGHT
    if direction == RIGHT:
        return DOWN
    if direction == DOWN:
        return LEFT
    if direction == LEFT:
        return UP
    return None

def find_guard(sitmap):
    """finds the guard in the situation map"""
    for (y, row) in enumerate(sitmap):
        for (x, item) in enumerate(row):
            if item == GUARD:
                return (x, y)
    return None

def guard_step(x, y, direction, sitmap):
    """makes the guard either take one step or rotate once"""
    if x + direction[0] >= 0 and x + direction[0] < len(sitmap[0]) and \
        y + direction[1] >= 0 and y + direction[1] < len(sitmap):
        if (sitmap[y + direction[1]][x + direction[0]]) == OBSTACLE:
            direction = rotate(direction)
            return x, y, direction, sitmap
    if sitmap[y][x] == "." or sitmap[y][x] == "^":
        sitmap[y][x] = [direction]
    else:
        if direction in sitmap[y][x]:
            raise Exception("Loop")
        sitmap[y][x].append(direction)
    x += direction[0]
    y += direction[1]
    return x, y, direction, sitmap

def count_visited(sitmap):
    """counts all the distinctly visited positions in sitmap"""
    result = 0
    for row in sitmap:
        for item in row:
            if item != "#" and item != ".":
                result += 1
    return result

def print_sitmap(sitmap):
    """Print the Situation map in a nice way"""
    for row in sitmap:
        for item in row:
            if isinstance(item, list):
                if (UP in item or DOWN in item) and (LEFT in item or RIGHT in item):
                    print("+", end="")
                elif UP in item or DOWN in item:
                    print("|", end="")
                elif LEFT in item or RIGHT in item:
                    print("-", end="")
            else:
                print(item, sep="", end="")
        print("")

def main():
    """It's the main function. Call with ./day06.py"""
    orig_sitmap = []
    with open(INPUT, 'r', encoding='utf-8') as inputfile:
        for line in inputfile:
            orig_sitmap.append(list(line.strip()))
    sitmap = copy.deepcopy(orig_sitmap)
    (x, y) = find_guard(sitmap)
    direction = UP
    while x < len(sitmap[0]) and x >= 0 and y < len(sitmap) and y >= 0:
        (x, y, direction, sitmap) = guard_step(x, y, direction, sitmap)
    part_one = count_visited(sitmap)
    part_two = 0
    for o_y in range(len(orig_sitmap)):
        for o_x in range(len(orig_sitmap[o_y])):
            print(o_x, o_y)
            if orig_sitmap[o_y][o_x] == "#" or orig_sitmap[o_y][o_x] == "^":
                continue
            sitmap = copy.deepcopy(orig_sitmap)
            sitmap[o_y][o_x] = OBSTACLE
            (x, y) = find_guard(sitmap)
            direction = UP
            try:
                while x < len(sitmap[0]) and x >= 0 and y < len(sitmap) and y >= 0:
                    (x, y, direction, sitmap) = guard_step(x, y, direction, sitmap)
            except Exception:
                part_two += 1
    print(f"distinct visited positions: {part_one}")
    print(f"possible loop obstacles: {part_two}")

if __name__ == "__main__":
    main()
