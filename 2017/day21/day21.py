#!/usr/bin/python3

STARTING_PATTERN=".#.\n..#\n###"
# pictures are strings, lines are \n separated

""" rotates a pattern clockwise """
def rotatePattern(pattern):
    result = ""
    lines = pattern.split("\n")
    size = len(lines[0])
    if size == 2:
        result = lines[1][0] + lines[0][0] + "\n" + lines[1][1] + lines[0][1]
    elif size == 3:
        result  = lines[2][0] + lines[1][0] + lines[0][0] + "\n"
        result += lines[2][1] + lines[1][1] + lines[0][1] + "\n"
        result += lines[2][2] + lines[1][2] + lines[0][2]
    elif size == 4:
        result  = lines[3][0] + lines[2][0] + lines[1][0] + lines[0][0] + "\n"
        result += lines[3][1] + lines[2][1] + lines[1][1] + lines[0][1] + "\n"
        result += lines[3][2] + lines[2][2] + lines[1][2] + lines[0][2] + "\n"
        result += lines[3][3] + lines[2][3] + lines[1][3] + lines[0][3]
    return result

def flipPatternH(pattern):
    result = ""
    lines = pattern.split("\n")
    size = len(lines[0])
    if size == 2:
        result = lines[1][0] + lines[1][1] + "\n" + lines[0][0] + lines[0][1]
    elif size == 3:
        result  = lines[2][0] + lines[2][1] + lines[2][2] + "\n"
        result += lines[1][0] + lines[1][1] + lines[1][2] + "\n"
        result += lines[0][0] + lines[0][1] + lines[0][2]
    elif size == 4:
        result  = lines[3][0] + lines[3][1] + lines[3][2] + lines[3][3] + "\n"
        result += lines[2][0] + lines[2][1] + lines[2][2] + lines[2][3] + "\n"
        result += lines[1][0] + lines[1][1] + lines[1][2] + lines[1][3] + "\n"
        result += lines[0][0] + lines[0][1] + lines[0][2] + lines[0][3]
    return result

def flipPatternV(pattern):
    result = ""
    lines = pattern.split("\n")
    size = len(lines[0])
    if size == 2:
        result = lines[0][1] + lines[0][0] + "\n" + lines[1][1] + lines[1][0]
    elif size == 3:
        result  = lines[0][2] + lines[0][1] + lines[0][0] + "\n"
        result += lines[1][2] + lines[1][1] + lines[1][0] + "\n"
        result += lines[2][2] + lines[2][1] + lines[2][0]
    elif size == 4:
        result  = lines[0][3] + lines[0][2] + lines[0][1] + lines[0][0] + "\n"
        result += lines[1][3] + lines[1][2] + lines[1][1] + lines[1][0] + "\n"
        result += lines[2][3] + lines[2][2] + lines[2][1] + lines[2][0] + "\n"
        result += lines[3][3] + lines[3][2] + lines[3][1] + lines[3][0]
    return result

def getInput(inputfile):
    result = {}
    with open(inputfile, 'r') as infile:
        for line in infile:
            splitline = line.strip().split(" => ")
            pattern = splitline[0].replace("/", "\n")
            replacement = splitline[1].replace("/", "\n")
            result[pattern] = replacement
    return result

def main():
    picture = STARTING_PATTERN
    patterns = getInput("input")
    # develop picture
    for turn in range(18):
        newPicture = [] # List of strings to be later concatenated
        lines = picture.split("\n")
        # determine "size"
        size = len(lines[0])
        line = 0
        if size % 2 == 0:
            patternSize = 2
        else:
            patternSize = 3
        while line*patternSize < size:
            pos = 0
            for i in range(patternSize +1):
                newPicture.append("")
            while (pos * patternSize < size):
                # get the (next) pattern
                pattern = ""
                for i in range(patternSize):
                    for j in range(patternSize):
                        pattern += lines[line * patternSize+ i][pos * patternSize + j]
                        if (j == (patternSize-1)) and (i != patternSize-1):
                            pattern += "\n"
                origPattern = pattern
                # pattern is now complete!
                rotations = 0
                replacement = ""
                while rotations < 4:
                    if pattern in patterns:
                        replacement = patterns[pattern]
                        break
                    else:
                        patternBefore = pattern
                        pattern = flipPatternH(patternBefore)
                        if pattern in patterns:
                            replacement = patterns[pattern]
                            break
                        else:
                            pattern = flipPatternV(patternBefore)
                            if pattern in patterns:
                                replacement = patterns[pattern]
                                break
                    pattern = rotatePattern(patternBefore)
                    rotations += 1
                # add replacement to newPicture
                splitReplacement = replacement.split("\n")
                for ix in range(patternSize + 1):
                    newPicture[line * (patternSize+1) + ix] += splitReplacement[ix]

                pos += 1
            line += 1

        picture = "\n".join(newPicture)
        if turn == 5-1:
            counter = 0
            for char in picture:
                if char == "#":
                    counter += 1
            print("Occurences of # after 5 recursions: %d" % counter)

    counter = 0
    for char in picture:
        if char == "#":
            counter += 1
    print("Occurences of # after 18 recursions: %d" % counter)

if __name__ == "__main__":
    main()
