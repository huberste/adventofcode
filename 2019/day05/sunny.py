#! /usr/bin/env python3

import intcode

INPUTFILE = 'input'
INPUT = 1 # Day 05: TEST the air conditioner unit
INPUT_TWO = 5 # Day 05: TEST the thermal radiators

def main():
    # read initial memory from input file
    input_file = open(INPUTFILE, 'r')
    line = input_file.readline().strip()
    input_file.close()
    memory = list(map(int, line.split(',')))

    result = intcode.calculate(memory, INPUT)
    print("Diagnostic code for the air conditioner: ", result)

    memory = list(map(int, line.split(',')))
    result = intcode.calculate(memory, INPUT_TWO)
    print("Diagnostic code for the thermal radiators: ", result)

if __name__ == "__main__":
    main()
