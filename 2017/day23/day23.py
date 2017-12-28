#!/usr/bin/python3

def getInput(infile):
    result = []
    with open(infile, "r") as inputfile:
        for line in inputfile:
            result.append(line.strip())
    return result

REGISTERS = "abcdefgh"

def main():
    instructions = getInput("input")
    registers = {}
    # part1
    for register in REGISTERS:
        registers[register] = 0
    mulcounter = 0
    index = 0

    while (index >=0) and (index < len(instructions)):
        instruction = instructions[index].split(" ")
        cmd = instruction[0]
        if cmd == "set":
            if instruction[2] in REGISTERS:
                result = registers[instruction[2]]
            else:
                result = int(instruction[2])
            registers[instruction[1]] = result
            index += 1
        elif cmd == "sub":
            add = 0
            if instruction[2] in REGISTERS:
                add = registers[instruction[2]]
            else:
                add = int(instruction[2])
            result = registers[instruction[1]] - add
            registers[instruction[1]] = result
            index = index + 1
        elif cmd == "mul":
            mul = 0
            mulcounter += 1
            if instruction[2] in REGISTERS:
                mul = registers[instruction[2]]
            else:
                mul = int(instruction[2])
            result = registers[instruction[1]] * mul
            registers[instruction[1]] = result
            index = index + 1
        elif cmd == "jnz":
            if instruction[1] in REGISTERS:
                if registers[instruction[1]] != 0:
                    if instruction[2] in REGISTERS:
                        index = index + registers[instruction[2]]
                    else:
                        index = index + int(instruction[2])
                else:
                    index = index + 1
            else:
                if int(instruction[1]) != 0:
                    if instruction[2] in REGISTERS:
                        index = index + registers[instruction[2]]
                    else:
                        index = index + int(instruction[2])
                else:
                    index = index + 1

    print("Part 1: invoked MUL = %d" % mulcounter)

    # part2
    # the code checks every 17th number between b and c if it's NOT a prime
    h = 0 # number of non-primes between b and c
    start = int(instructions[0].split()[2]) * int(instructions[4].split()[2]) - int(instructions[5].split()[2])
    for x in range(start, start + 17001, 17):
        for i in range(2,x):
            if x % i == 0: # not a prime!
                h += 1
                break
    print("Part 2: value of register h: %d" % h)

if __name__ == "__main__":
    main()
