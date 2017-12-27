#!/usr/bin/python3

# load inputdata from file
with open('input', 'r') as inputfile:
	jumplist = []
	for line in inputfile:
		jumplist.append(int(line.strip()))
	instruction = 0
	ctr = 0
	while (instruction >= 0) and (instruction < len(jumplist)):
		tmp = instruction
		instruction = instruction + jumplist[instruction]
		jumplist[tmp] = jumplist[tmp] + 1
		ctr = ctr + 1

print("steps needed for part 1: %d" % ctr)	

with open('input', 'r') as inputfile:
	jumplist = []
	for line in inputfile:
		jumplist.append(int(line.strip()))
	instruction = 0
	ctr = 0
	while (instruction >= 0) and (instruction < len(jumplist)):
		tmp = instruction
		instruction = instruction + jumplist[instruction]
		if (jumplist[tmp]>=3):
			jumplist[tmp] = jumplist[tmp] - 1
		else:
			jumplist[tmp] = jumplist[tmp] + 1
		ctr = ctr + 1

	print("steps needed for part 2: %d" % ctr)	
