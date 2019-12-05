#! /usr/bin/env python3

INPUTFILE = 'input'

OUTPUT_POINTER = 0

def calculate(memory):
    instruction_pointer = 0
    running = True
    while running:
        opcode = memory[instruction_pointer]

        if opcode == 1:
            # add
            result = memory[memory[instruction_pointer+1]] + memory[memory[instruction_pointer+2]]
            memory[memory[instruction_pointer+3]] = result
            instruction_pointer += 4
        elif opcode == 2:
            # multiply
            result = memory[memory[instruction_pointer+1]] * memory[memory[instruction_pointer+2]]
            memory[memory[instruction_pointer+3]] = result
            instruction_pointer += 4
        elif opcode == 99:
            # halt
            running = False
        else:
            # something went wrong
            print("something went wrong.")
            running = False
    return memory[OUTPUT_POINTER]

def main():
    # read initial memory from input file
    input_file = open(INPUTFILE, 'r')
    line = input_file.readline().strip()
    input_file.close()
    memory = list(map(int, line.split(',')))

    # part 1
    # set memory to 1202 error (day 02 special)
    noun = 12
    verb = 2

    memory[1] = noun
    memory[2] = verb

    result = calculate(memory)

    print("Part 1: Result with Input 1202: " + str(result))

    # part 2: which verb / noun give the answer?
    answer = 19690720

    for verb in range(0, 100, 1):
        for noun in range(0, 100, 1):
            # reset memory
            memory = list(map(int, line.split(',')))
            memory[1] = verb
            memory[2] = noun
            result = calculate(memory)
            if result == answer:
                print("Part 2: 100 * verb + noun =", 100*verb+noun)
                return

if __name__ == "__main__":
    main()
