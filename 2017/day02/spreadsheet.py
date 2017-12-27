#!/usr/bin/python3

import sys;

# part 1: calculate the checksum =SUM(max - min)
# part 2: calculate the division-sum = SUM(div1 / div2) where div1 % div2 = 0
# load inputdata from file
with open('input', 'r') as inputfile:
	checksum = 0
	divisionsum = 0
	i = 0
	for line in inputfile:
		min = sys.maxsize
		max = 0
		for number in line.strip().split('\t'):
			if int(number) < min:
				min = int(number)
			if int(number) > max:
				max = int(number)
			for number2 in line.strip().split('\t'):
				if (int(number) != int(number2)) & ((int(number) % int(number2)) == 0):
					print("line number %d: found division: %d / %d" % (i, int(number), int(number2)))
					divisionsum = divisionsum + (int(number) / int(number2))
		checksum = checksum + (max - min)
		i = i+1

	print("checksum: %d" % checksum)
	print("divisionsum: %d" % divisionsum)
			

# part 2
