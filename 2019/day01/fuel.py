#! /usr/bin/env python3

def fuel_fun(mass):
    result = (mass / 3) - 2
    if result < 0:
        result = 0
    return int(result)

# Test cases
#mass = 12
#mass = 14
#mass = 1969
#mass = 100756

f = open('input', 'r')
result_1 = 0
result_2 = 0
line = f.readline()
while line:
    mass = int(line)
    fuel = fuel_fun(mass)
    result_1 += fuel
    while fuel > 0:
        result_2 += fuel
        fuel = fuel_fun(fuel)
    line = f.readline()

print("Fuel needed for the rocket: " + str(result_1))
print("Fuel needed for the rocket (including fuel): " + str(result_2))