#!/usr/bin/python3

def getInput(infile):
    result = []
    with open(infile, "r") as inputfile:
        for line in inputfile:
            result.append(line.strip())
    return result

alphabet = "abcdfip"
registersA = {}
sentA = []
registersB = {}
sentB = []
iA = 0
iB = 0
waitA = False
waitB = False

def stepA(instruction, iA, ctrA, part1):
    instruction = instruction.split(" ")
    cmd = instruction[0]
    waitA = False
    if cmd == "snd":
        if instruction[1] in alphabet:
            snd = registersA[instruction[1]]
        else:
            snd = int(instruction[1])
        sentA.append(snd)
        ctrA = ctrA + 1
        WaitB = False
        iA = iA + 1
    elif cmd == "set":
        if instruction[2] in alphabet:
            result = registersA[instruction[2]]
        else:
            result = int(instruction[2])
        registersA[instruction[1]] = result
        iA = iA + 1
    elif cmd == "add":
        add = 0
        if instruction[2] in alphabet:
            add = registersA[instruction[2]]
        else:
            add = int(instruction[2])
        result = registersA[instruction[1]] + add
        registersA[instruction[1]] = result
        iA = iA + 1
    elif cmd == "mul":
        mul = 0
        if instruction[2] in alphabet:
            mul = registersA[instruction[2]]
        else:
            mul = int(instruction[2])
        result = registersA[instruction[1]] * mul
        registersA[instruction[1]] = result
        iA = iA + 1
    elif cmd == "mod":
        mod = 0 
        if instruction[2] in alphabet:
            mod = registersA[instruction[2]]
        else:
            mod = int(instruction[2])
        result = registersA[instruction[1]] % mod
        registersA[instruction[1]] = result
        iA = iA + 1
    elif cmd == "rcv":
        if part1:
            print("answer for part1: %d" % sentA[len(sentA)-1])
            part1 = False
        if len(sentB) < 1:
            waitA = True
        else:
            rcv = sentB.pop(0)
            registersA[instruction[1]] = rcv
            iA = iA + 1
    elif cmd == "jgz":
        if instruction[1] in alphabet:
            if registersA[instruction[1]] > 0:
                if instruction[2] in alphabet:
                    iA = iA + registersA[instruction[2]]
                else:
                    iA = iA + int(instruction[2])
            else:
                iA = iA + 1
        else:
            if int(instruction[1]) > 0:
                if instruction[2] in alphabet:
                    iA = iA + registersA[instruction[2]]
                else:
                    iA = iA + int(instruction[2])
            else:
                iA = iA + 1

    return (iA, waitA, ctrA, part1)
    

def stepB(instruction, iB, ctrB):
    instruction = instruction.split(" ")
    cmd = instruction[0]
    waitB = False
    if cmd == "snd":
        if instruction[1] in alphabet:
            snd = registersB[instruction[1]]
        else:
            snd = int(instruction[1])
        sentB.append(snd)
        ctrB = ctrB + 1
        iB = iB + 1
    elif cmd == "set":
        if instruction[2] in alphabet:
            result = registersB[instruction[2]]
        else:
            result = int(instruction[2])
        registersB[instruction[1]] = result
        iB = iB + 1
    elif cmd == "add":
        add = 0
        if instruction[2] in alphabet:
            add = registersB[instruction[2]]
        else:
            add = int(instruction[2])
        result = registersB[instruction[1]] + add
        registersB[instruction[1]] = result
        iB = iB + 1
    elif cmd == "mul":
        mul = 0
        if instruction[2] in alphabet:
            mul = registersB[instruction[2]]
        else:
            mul = int(instruction[2])
        result = registersB[instruction[1]] * mul
        registersB[instruction[1]] = result
        iB = iB + 1
    elif cmd == "mod":
        mod = 0 
        if instruction[2] in alphabet:
            mod = registersB[instruction[2]]
        else:
            mod = int(instruction[2])
        result = registersB[instruction[1]] % mod
        registersB[instruction[1]] = result
        iB = iB + 1
    elif cmd == "rcv":
        if len(sentA) < 1:
            waitB = True
        else:
            rcv = sentA.pop(0)
            registersB[instruction[1]] = rcv
            iB = iB + 1
    elif cmd == "jgz":
        if instruction[1] in alphabet:
            if registersB[instruction[1]] > 0:
                if instruction[2] in alphabet:
                    iB = iB + registersB[instruction[2]]
                else:
                    iB = iB + int(instruction[2])
            else:
                iB = iB + 1
        else:
            if int(instruction[1]) > 0:
                if instruction[2] in alphabet:
                    iB = iB + registersB[instruction[2]]
                else:
                    iB = iB + int(instruction[2])
            else:
                iB = iB + 1
                
    return (iB, waitB, ctrB)

def main():
    instructions = getInput("input")
    for register in alphabet:
        registersA[register] = 0
        registersB[register] = 0
        if register == "p":
            registersB[register] = 1
    result = 0
    iA = 0
    iB = 0
    waitA = False
    waitB = False
    ctrA = 0
    ctrB = 0
    part1 = True
    while (iA>=0) and (iA < len(instructions)):
        if waitA and (len(sentB) > 0):
            waitA = False
        if waitB and (len(sentA) > 0):
            waitB = False
        if waitA and waitB:
            #print("deadlock!")
            break
        elif waitA:
            if (iB >= 0) and (iB < len(instructions)):
                (iB, waitB, ctrB) = stepB(instructions[iB], iB, ctrB)
            else:
                print("B terminates...")
        else:
            (iA, waitA, ctrA, part1) = stepA(instructions[iA], iA, ctrA, part1)
            
    print("answer for part2: %d" % ctrB)

if __name__ == "__main__":
    main()
