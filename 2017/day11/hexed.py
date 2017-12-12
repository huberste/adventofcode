#!/usr/bin/python3

def getInput(inptfl):
	result = []
	with open(inptfl, 'r') as inputfile:
		for line in inputfile:
			for direction in line.strip().split(','):
				result.append(direction)
	return result

def main():
	inpt = getInput("input")
	n = 0.0
	e = 0.0
	s = 0.0
	w = 0.0
	furthest = 0.0
	for direction in inpt:
		if direction == "n":
			n = n + 1.0
		elif direction =="ne":
			n = n + 0.5
			e = e + 1.0
		elif direction == "se":
			s = s + 0.5
			e = e + 1.0
		elif direction == "s":
			s = s + 1.0
		elif direction == "sw":
			s = s + 0.5
			w = w + 1.0
		elif direction == "nw":
			n = n + 0.5
			w = w + 1.0
		ntemp = abs(n - s)
		etemp = abs(e - w)
		ntemp = ntemp - 0.5 * etemp
		if (ntemp + etemp) > furthest:
			furthest = ntemp + etemp

	n = abs(n - s)
	e = abs(e - w)
	n = n - 0.5 * e
	minsteps = n + e
	print("minimum number of steps: %d" % minsteps)
	print("furthest distance: %d" % furthest)

if __name__ == "__main__":
	main()
	
