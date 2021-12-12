#!/usr/bin/env python3

def decode_line(patterns, output):
    result = 0
    decoded = {}
    coded = {}
    # find 1,4,7,8: for easy patterns:
    for pattern in patterns:
        if len(pattern) == 2:
            decoded[pattern] = 1
            coded[1] = pattern
        elif len(pattern) == 3:
            decoded[pattern] = 7
            coded[7] = pattern
        elif len(pattern) == 4:
            decoded[pattern] = 4
            coded[4] = pattern
        elif len(pattern) == 7:
            decoded[pattern] = 8
            coded[8] = pattern
    # find 3: len = 5 and 1 in 3
    for pattern in patterns:
        three_possible = True
        if len(pattern) == 5:
            for segment in coded[1]:
                if not segment in pattern:
                    three_possible = False
            if three_possible:
                decoded[pattern] = 3
                coded[3] = pattern
                break
    # find 9: len = 6 and 3 in 9
    for pattern in patterns:
        nine_possible = True
        if len(pattern) == 6:
            for segment in coded[3]:
                if not segment in pattern:
                    nine_possible = False
            if nine_possible:
                decoded[pattern] = 9
                coded[9] = pattern
                break
    # find 0: it's len == 6, it's not 9 but contains 1
    for pattern in patterns:
        zero_possible = True
        if len(pattern) == 6:
            for segment in coded[1]:
                if not segment in pattern:
                    zero_possible = False
            if zero_possible:
                if not pattern in decoded:
                    decoded[pattern] = 0
                    coded[0] = pattern
                    break
    # find 6: last pattern with 6 segments
    for pattern in patterns:
        if len(pattern) == 6:
            if not pattern in decoded:
                decoded[pattern] = 6
                coded[6] = pattern
                break
    # find lower left segment: 8-9
    segment_e = ""
    for eight_segment in coded[8]:
        if eight_segment not in coded[9]:
            segment_e = eight_segment
            break
    # find 2: 5-segment with segment_e
    for pattern in patterns:
        if len(pattern) == 5:
            if segment_e in pattern:
                decoded[pattern] = 2
                coded[2] = pattern
                break
    # find 5: last segment
    for pattern in patterns:
        if not pattern in decoded:
            decoded[pattern] = 5
            coded[5] = pattern

    for digit in output:
        print
        result = 10* result
        result += decoded[digit]
    return result


def main():
    f = open('input', 'r')
    # list of all patterns and outputs
    patterns = []
    outputs = []
    line = f.readline().rstrip()
    while line:
        parts = line.split(" | ")
        patterns.append(list(map("".join, list(map(sorted, parts[0].split())))))
        outputs.append(list(map("".join, list(map(sorted, parts[1].split())))))
        line = f.readline().rstrip()
    f.close()
    
    count_simple = 0
    for output in outputs:
        for signal in output:
            if len(signal) in (2,3,4,7):
                count_simple += 1
    print("simple patterns in outputs:", count_simple)

    sum = 0
    for i in range(len(patterns)):
        sum += decode_line(patterns[i], outputs[i])
    print(sum)

if __name__ == "__main__":
    main()