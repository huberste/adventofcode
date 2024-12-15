#! /usr/bin/env python3
"""Module for solving advent of code 2024/10"""

INPUT = "day10.input"

def find_good_trails(topomap, x, y, num):
    if num == 9:
        return [(x,y)]
    result = []
    next_num = num + 1
    # search north
    if y > 0:
        if topomap[y-1][x] == next_num:
            result.extend(find_good_trails(topomap, x, y-1, next_num))
    # search east
    if x < len(topomap[y]) - 1:
        if topomap[y][x+1] == next_num:
            result.extend(find_good_trails(topomap, x+1, y, next_num))
    # search south
    if y < len(topomap) - 1:
        if topomap[y+1][x] == next_num:
            result.extend(find_good_trails(topomap, x, y+1, next_num))
    # search west
    if x > 0:
        if topomap[y][x-1] == next_num:
            result.extend(find_good_trails(topomap, x-1, y, next_num))
    return result

def find_trails(topomap):
    part_one = 0
    part_two = 0
    for y, row in enumerate(topomap):
        for x, height in enumerate(row):
            if height == 0:
                # found trail start
                trails = find_good_trails(topomap, x, y, 0)
                ranking = len(trails)
                part_two += ranking
                score = len(sorted(set(trails)))
                part_one += score
    print(f"Sum of the scores of all trailheads: {part_one}")
    print(f"Sum of the ratings of all trailheads: {part_two}")

def main():
    """It's the main function. Call with ./day10.py"""
    topomap = []
    with open(INPUT, 'r', encoding='utf-8') as inputfile:
        for line in inputfile:
            topomap.append(list(map(int, list(line.strip()))))
    find_trails(topomap)
    

if __name__ == "__main__":
    main()
