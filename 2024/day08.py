#! /usr/bin/env python3
"""Module for solving advent of code 2024/08"""

INPUT = "day08.input"

def count_antinodes(nodemap):
    """counts all the antinodes in the nodemap"""
    result = 0
    for _, row in enumerate(nodemap):
        for _, point in enumerate(row):
            if point is not None:
                result += 1
    return result

def main():
    """It's the main function. Call with ./day08.py"""
    antmap = []
    with open(INPUT, 'r', encoding='utf-8') as inputfile:
        for line in inputfile:
            antmap.append(list(line.strip()))
    # create map of nodes (which is empty at the start)
    nodemap = []
    harmonic_nodemap = []
    for row in antmap:
        nodemap.append( [None] * len(row) )
        harmonic_nodemap.append( [None] * len(row) )
    # create dict antennas: { frequency: [(x, y), ...], ...}
    antennas = {}
    for y, row in enumerate(antmap):
        for x, point in enumerate(row):
            if point == ".":
                continue
            if not point in antennas:
                antennas[point] = []
            antennas[point].append((x, y))
    for frequency, positions in antennas.items():
        for num, pos_a in enumerate(positions):
            for b in range(num+1, len(positions)):
                pos_b = positions[b]
                dist_x = pos_b[0] - pos_a[0]
                dist_y = pos_b[1] - pos_a[1]
                ### PART ONE
                new_x = pos_a[0] - dist_x
                new_y = pos_a[1] - dist_y
                if 0 <= new_y < len(nodemap) and \
                   0 <= new_x < len(nodemap[new_y]):
                    nodemap[new_x][new_y] = frequency
                new_x = pos_b[0] + dist_x
                new_y = pos_b[1] + dist_y
                if 0 <= new_y < len(nodemap) and \
                   0 <= new_x < len(nodemap[new_y]):
                    nodemap[new_x][new_y] = frequency
                ### PART TWO
                new_x = pos_a[0]
                new_y = pos_a[1]
                while 0 <= new_y < len(nodemap) and \
                      0 <= new_x < len(nodemap[new_y]):
                    harmonic_nodemap[new_x][new_y] = frequency
                    new_x = new_x - dist_x
                    new_y = new_y - dist_y
                new_x = pos_b[0]
                new_y = pos_b[1]
                while 0 <= new_y < len(nodemap) and \
                      0 <= new_x < len(nodemap[new_y]):
                    harmonic_nodemap[new_x][new_y] = frequency
                    new_x = new_x + dist_x
                    new_y = new_y + dist_y
    part_one = count_antinodes(nodemap)
    print(f"number of antinodes: {part_one}")
    part_two = count_antinodes(harmonic_nodemap)
    print(f"number of harmonic antinodes: {part_two}")

if __name__ == "__main__":
    main()
