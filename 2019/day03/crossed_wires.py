#! /usr/bin/env python3

INPUTFILE = 'input'

def main():
    # read initial memory from input file
    input_file = open(INPUTFILE, 'r')
    wire_one = input_file.readline().strip().split(',')
    wire_two = input_file.readline().strip().split(',')
    input_file.close()

    min_distance = float('inf')
    min_steps = float('inf')
    w1x = 0
    w1y = 0
    steps1 = 0
    i = 0
    for w1_dir in wire_one:
        i = i + 1
        # make one step, trace complete wire 2 to see if it intersects.
        direction_w1 = w1_dir[:1]
        length_w1 = int(w1_dir[1:])
        # print progress:
        print ("[PROGRESS] Direction", i, "of", len(wire_one), "step", length_w1)
        while length_w1 > 0:
            length_w1 -= 1
            steps1 += 1
            if direction_w1 == 'L':
                w1x -= 1
            elif direction_w1 == 'R':
                w1x += 1
            elif direction_w1 == 'U':
                w1y += 1
            elif direction_w1 == 'D':
                w1y -= 1
            else:
                print("oops. The direction", direction_w1, "does not make sense...")
                return

            w2x = 0
            w2y = 0
            steps2 = 0
            j = 0
            for w2_dir in wire_two:
                j = j + 1
                # make one step, trace complete wire 2 to see if it intersects.
                direction_w2 = w2_dir[:1]
                length_w2 = int(w2_dir[1:])
                while length_w2 > 0:
                    length_w2 -= 1
                    steps2 += 1
                    if direction_w2 == 'L':
                        w2x -= 1
                    elif direction_w2 == 'R':
                        w2x += 1
                    elif direction_w2 == 'U':
                        w2y += 1
                    elif direction_w2 == 'D':
                        w2y -= 1
                    else:
                        print("oops. The direction", direction_w2, "does not make sense...")
                        return

                    if w1x == w2x and w1y == w2y:
                        distance = abs(w1x)+abs(w1y)
                        steps = steps1 + steps2
                        print("the wires cross at", w1x, ",", w1y, ", distance is", distance, "steps:", steps)
                        if distance < min_distance:
                            min_distance=distance
                        if steps < min_steps:
                            min_steps=steps
                        
    print("Min distance:", min_distance)
    print("Min steps:", min_steps)


if __name__ == "__main__":
    main()
