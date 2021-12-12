#!/usr/bin/env python3

INPUTFILE = "input"
ILLEGAL_POINTS = { ")": 3, "]": 57, "}": 1197, ">": 25137}
COMPLETION_POINTS = {"(": 1, "[": 2, "{": 3, "<": 4}
OPENERS = { "(": ")", "[": "]", "{": "}", "<": ">"}

def check_syntax(line):
    illegal_score = 0
    completion_score = 0
    opened = []
    for char in line:
        if char in OPENERS:
            opened.append(char)
        else:
            last = opened.pop()
            if OPENERS[last] != char:
                # illegal!
                illegal_score += ILLEGAL_POINTS[char]
                break
    if illegal_score == 0:
        while len(opened) > 0:
            char = opened.pop()
            completion_score = 5 * completion_score + COMPLETION_POINTS[char]

    return (illegal_score, completion_score)

def main():
    f = open(INPUTFILE, 'r')
    lines = []
    line = f.readline().rstrip()
    while line:
        lines.append(list(line))
        line = f.readline().rstrip()
    f.close()
    illegal_score_sum = 0
    completion_scores = []
    for line in lines:
        illegal_score, completion_score = check_syntax(line)
        if illegal_score > 0:
            illegal_score_sum += illegal_score
        else:
            completion_scores.append(completion_score)
    print("Part 1: Sum of illegal scores =", illegal_score_sum)
    completion_scores.sort()
    print("Part 2: middle completion score =", completion_scores[int((len(completion_scores)-1)/2)])

if __name__ == "__main__":
    main()