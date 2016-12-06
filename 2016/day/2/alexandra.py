#!/usr/bin/python3

# Python3 script to solve part one of day 2 of the
# AdventOfCode 2016
# http://adventofcode.com/
#
# author Alexandra Meyer


#part 1
# load inputdata from file
point=5
with open('input', 'r') as inputfile:
	for line in inputfile:
		#print(line)
		for char in line:
			#print(char)
			if char == "U":
				if point < 4 :
					continue
				point -= 3
			elif char == "D":
				if point >6 :
					continue
				point += 3
			elif char == "R" :
				if (point % 3) == 0 :
					continue
				point += 1
			elif char == "L" :
				if (point % 3) == 1:
					continue
				point -= 1
		print(str(point))
		
			
print("Part2:")		
#part 2			
#		1  2  3  4  5   if !(i in (3 7 9 11 15))
#		6  7  8  9  10
#		11 12 13 14 15
#		16 17 18 19 20
#		21 22 23 24 25

keypad = "  1   234 56789 ABC   D  "

#load inputdata from file	
point=13

with open('input', 'r') as inputfile:
	for line in inputfile:
		#print(line)
		for char in line:
			#print(char)
			if char == "U":
				if not(point in (3, 7, 9, 11, 15)):
					point -= 5
			elif char == "D":
				if not(point in (11, 17, 23, 19, 15)) :
					point += 5
			elif char == "R" :
				if not(point in (3, 9, 15, 19, 23)):
					point += 1
			elif char == "L" :
				if not(point in (3, 7, 11, 17, 23)):
					point -= 1


		print (keypad[point-1])
		
		if point ==3:
			print('1')
		elif point <10:
		    print(str(point-5))
		elif point < 16 :
			print(str(point-6))
		elif point == 17:
			print("A")
		elif point == 18 :
			print("B")
		elif point == 19:
			print("C")
		else :
			print("D")
			
			
