#!/usr/bin/python3

import sys
import math

FIRST_VALUE_A = 277
FIRST_VALUE_B = 349

FACTOR_A = 16807
FACTOR_B = 48271

CRITERION_A = 4
CRITERION_B = 8

DIVISOR = 2147483647

COMPARED_BITS = 16
COMPARED_VALUES_A = 40000000
COMPARED_VALUES_B = 5000000

def judge(valueA, valueB):
	return (valueA % (math.pow(2, COMPARED_BITS))) == (valueB % (math.pow(2, COMPARED_BITS)))

def part1():
	judgeCtr = 0
	prevValueA = FIRST_VALUE_A
	prevValueB = FIRST_VALUE_B
	for i in range(COMPARED_VALUES_A):
		# generatorA
		valueA = (prevValueA * FACTOR_A) % DIVISOR
		prevValueA = valueA
		# generatorB
		valueB = (prevValueB * FACTOR_B) % DIVISOR
		prevValueB = valueB
		# compare
		if judge(valueA, valueB):
			judgeCtr = judgeCtr + 1

	print("Judge's final count (part1): %d" % judgeCtr)

def part2():
	judgeCtr = 0
	prevValueA = FIRST_VALUE_A
	prevValueB = FIRST_VALUE_B
	for i in range(COMPARED_VALUES_B):
		# generatorA
		generate = True
		while generate:
			valueA = (prevValueA * FACTOR_A) % DIVISOR
			prevValueA = valueA
			if (valueA % CRITERION_A == 0):
				generate = False
		# generatorB
		generate = True
		while generate:
			valueB = (prevValueB * FACTOR_B) % DIVISOR
			prevValueB = valueB
			if (valueB % CRITERION_B == 0):
				generate = False

		# compare
		if judge(valueA, valueB):
			judgeCtr = judgeCtr + 1

	print("Judge's final count (part2): %d" % judgeCtr)

def main():
	part1()
	part2()

if __name__ == "__main__":
	main()
