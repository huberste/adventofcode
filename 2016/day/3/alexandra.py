#!/usr/bin/python3

# Python3 script to solve part one of day 3 of the
# AdventOfCode 2016
# http://adventofcode.com/
#
# author Alexandra Meyer


#part 1
# AnzDr = Anzahl der Dreiecke
AnzDr = 0 
# load inputdata from file
with open('input', 'r') as inputfile:
	for line in inputfile:
		#print(line)
		numbers=[]
		for number in line.split():
			numbers.append(int(number))
		
		numbers.sort()
		if (numbers[0] + numbers[1] > numbers[2]):
			AnzDr += 1

print("result part one: " + str(AnzDr))

#part 2
# AnzDr = Anzahl der Dreiecke
AnzDr = 0 
numbers = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
row = 0;
with open('input', 'r') as inputfile:
	for line in inputfile:
		col = 0
		for number in line.split():
			numbers[col][row] =int(number)
			col +=1
		
		if (row == 2):
			zwischen = 0
			while zwischen < 3:
				nums = sorted(numbers[zwischen])
				if (nums[0] + nums[1] > nums[2]):
					AnzDr += 1
				zwischen+=1
		
		row = (row+1)%3
		
print("result part two: " + str(AnzDr))
