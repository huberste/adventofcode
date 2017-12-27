#!/usr/bin/bash

#read input and set registers:
registers  = {}
inputs = []
with open('input','r') as inputfile:
    for line in inputfile:
        splitline = line.strip().split()
        # we might null them more than once, but it's still faster than checking if it's already in the set...
        registers[splitline[0]] = 0
        inputs.append(splitline)

#calculate
maxOverall = -9999999
for line in inputs:
    print("line:", line	)
    #a line looks like this: 'b inc 5 if a > 1'
    register = line[0]
    operation = line[1]
    summand = int(line[2])
    #if = line[3]
    conditionRegister = line[4]
    condition = line[5]
    conditionValue = int(line[6])
    #determine if condition is met
    #this could also be done with eval()...
    conditionMet = False
    if condition == '>':
        conditionMet = registers[conditionRegister] > conditionValue
    elif condition == '<':
        conditionMet = registers[conditionRegister] < conditionValue
    elif condition == '==':
        conditionMet = registers[conditionRegister] == conditionValue
    elif condition == '!=':
        conditionMet = registers[conditionRegister] != conditionValue
    elif condition == '<=':
        conditionMet = registers[conditionRegister] <= conditionValue
    elif condition == '>=':
        conditionMet = registers[conditionRegister] >= conditionValue

    #execute! (or not)
    if conditionMet:
        if operation == 'inc':
            registers[register] = registers[register] + summand
        elif operation == 'dec':
            registers[register] = registers[register] - summand

    if maxOverall < registers[register]:
        maxOverall = registers[register]

#determine largest value
#int.MinVal would be better here...
max = -9999999
for register in registers:
    if max < registers[register]:
        max = registers[register]

print("largest register value at the end: %d" % max)
print("largest register value ever: %d" % maxOverall)
