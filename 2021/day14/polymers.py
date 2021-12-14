#!/usr/bin/env python3

INPUTFILE = "input"
STEPS_PART_ONE = 10
STEPS_PART_TWO = 40

def main():
    polymer = ""
    pairs = {}
    letters = {}
    insertions = {}
    f = open(INPUTFILE, 'r')
    polymer = f.readline().rstrip()
    line = f.readline().rstrip()
    line = f.readline().rstrip()
    while line:
        insertion = line.split(" -> ")
        insertions[insertion[0]] = insertion[1]
        pairs[insertion[0]] = 0
        line = f.readline().rstrip()
    f.close()
    for index in range(len(polymer) -1):
        pairs[polymer[index:index+2]] += 1
    for index in range(len(polymer)):
        if polymer[index] in letters:
            letters[polymer[index]] += 1
        else:
            letters[polymer[index]] = 1
    loop = 0
    while loop < STEPS_PART_TWO:
        index = 0
        pairs_new = {}
        for pair in insertions.keys():
            num = 0
            if pair in pairs:
                num = pairs[pair]
            # first new pair
            for new_pair in [pair[0] + insertions[pair], insertions[pair] + pair[1]]:
                if new_pair in pairs_new:
                    pairs_new[new_pair] += num
                else:
                    pairs_new[new_pair] = num
            if insertions[pair] in letters:
                letters[insertions[pair]] += num
            else:
                letters[insertions[pair]] = num
        pairs = pairs_new
        loop += 1
        if loop == STEPS_PART_ONE:
            max = 0
            maxletter = ""
            min = 999999999999999
            minletter = ""
            for letter in letters:
                if letters[letter] > max:
                    max = letters[letter]
                    maxletter = letter
                if letters[letter] < min:
                    min = letters[letter]
                    minletter = letter
            print("most_common - least_common after", STEPS_PART_ONE, "steps:", max-min)

    print(pairs)
    print(letters)
    max = 0
    maxletter = ""
    min = float('inf')
    minletter = ""
    for letter in letters:
        if letters[letter] > max:
            max = letters[letter]
            maxletter = letter
        if letters[letter] < min:
            min = letters[letter]
            minletter = letter
    print("most_common - least_common:", max-min)

if __name__ == "__main__":
    main()