#!/usr/bin/python3

# load inputdata from file
weights = {}
programs = {}
with open('input', 'r') as inputfile:
	for line in inputfile:
		parts = line.strip().split("->")
		left = parts[0].strip().split()
		name = left[0]
		weight = int(left[1].replace("(","").replace(")",""))
		weights[name] = weight
		if len(parts) > 1:
			right = parts[1].strip().split()
			programs[name] = right
		else:
			programs[name] = ()

for programa in programs:
	notroot = False
	for programb in programs:
		print("subprograms:", programs[programb])
		notroot = notroot or (programa in programs[programb])
	if not notroot:
		print("root:", programa)
	
	
