#! /usr/bin/env python3

def is_safe(report):
    direction = None
    j = 0
    while j < len(report) - 1:
        if j == 0:
            if report[j] < report[j+1]:
                direction = 1
            else:
                direction = -1
        dist = (report[j+1] - report[j])
        dist = dist * direction
        if dist < 1 or dist > 3:
            return False
        j += 1
    return True

def main():
    reports = []
    with open('day02.input', 'r') as inputfile:
        for line in inputfile:
            reports.append(list(map(int,line.strip().split())))
    part_one = 0
    part_two = 0
    for report in reports:
        if is_safe(report):
            part_one += 1
        # just brute force it, it's not too many levels per report
        if any(is_safe(report[:i] + report[i+1:]) for i in range(len(report))):
            part_two += 1
            
    print("Number of safe reports: %d" % part_one)
    print("Number of safe reports with dampener enabled: %d" % part_two)

if __name__ == "__main__":
    main()