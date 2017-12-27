#!/usr/bin/python3

# load inputdata from file
inputfile = open('input', 'r')
inputdata = inputfile.readline().strip()
inputfile.close()

# part 1
sum = 0
lastchar = inputdata[len(inputdata) -1]

for char in inputdata:
	# debug: print character
	#print("[DEBUG] char = " + char)
	if char in ('0','1','2','3','4','5','6','7','8','9'):
		if int(char) == int(lastchar):
			sum = sum + int(char)
	#print("[DEBUG] sum is now " + str(sum))
	lastchar = char

print("sum for part 1: " + str(sum))

# part 2
sum = 0
length = len(inputdata)

for i in range(0,length -1):
	if int(inputdata[i]) == int(inputdata[(i + (length / 2)) % length]):
		sum = sum + int(inputdata[i])

print("sum for part 2: " + str(sum))
