#! /usr/bin/env python3

def main():
    leftlist = []
    rightlist = []
    with open('day01.input', 'r') as inputfile:
        for line in inputfile:
            line = line.strip().split()
            leftlist.append(int(line[0]))
            rightlist.append(int(line[1]))
    leftlist.sort()
    rightlist.sort()
    part_one = 0
    part_two = 0
    for i in range(len(leftlist)):
        part_one += abs(leftlist[i] - rightlist[i])
        part_two += leftlist[i] * rightlist.count(leftlist[i])
    print("Solution for part 1: %d" % part_one)
    print("Solution for part 2: %d" % part_two)

if __name__ == "__main__":
    main()