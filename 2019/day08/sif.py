#!/usr/bin/env python3

INPUTFILE = 'input'
COLS = 25
ROWS = 6

def main():
    # get input program
    input_file = open(INPUTFILE, 'r')
    line = input_file.readline().strip()
    input_file.close()
    # Find layer with fewest 0 digits
    num_layers = int(len(line) / (COLS * ROWS))
    min_zeroes = COLS * ROWS
    min_zeroes_layer = 0
    min_zeroes_layer_count = []
    result = [2] * COLS * ROWS
    for layer in range(num_layers):
        pixels = line[layer * COLS * ROWS: (layer + 1) * COLS * ROWS]
        count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for i in range(COLS * ROWS):
            count[int(pixels[i])] += 1
            if result[i] == 2:
                result[i] = int(pixels[i])
        if count[0] < min_zeroes:
            min_zeroes = count[0]
            min_zeroes_layer = layer
            min_zeroes_layer_count = count
    # multiply number of 1 pixels with number of 2 pixels
    print(min_zeroes_layer_count[1] * min_zeroes_layer_count[2])
    for i in range(ROWS):
        for j in range(COLS):
            if result[i*COLS + j] == 0:
                print(" ", end="")
            else:
                print("0", end="")
        print("")

if __name__ == "__main__":
    main()
