#!/usr/bin/python3

# load inputdata from file

def readInput(input):
	weights = {}
	programs = {}
	with open(input, 'r') as inputfile:
		for line in inputfile:
			parts = line.strip().split("->")
			left = parts[0].strip().split()
			name = left[0]
			weight = int(left[1].replace("(","").replace(")",""))
			weights[name] = weight
			if len(parts) > 1:
				right = parts[1].strip().split(", ")
				programs[name] = right
			else:
				programs[name] = ()
	return (weights, programs)

def findroot(programs):
	root = ""
	for programa in programs:
		notroot = False
		for programb in programs:
			if programa in programs[programb]:
				notroot = True
				break;
		if not notroot:
			root = programa
			break
	return root

def weightOfSubTower(weights, programs, program):
	result = weights[program]
	for subprogram in programs[program]:
		result = result + weightOfSubTower(weights, programs, subprogram)
	return result

def weightsOfSubTowers(weights, programs, program):
	result = []
	for subprogram in programs[program]:
		result.append((subprogram, weightOfSubTower(weights, programs, subprogram)))
	return result

def findHighestUnbalance(weights, programs, root):
	result = ()
	weightsOfSubTwrs = weightsOfSubTowers(weights, programs, root)
	temp = []
	balanced_weight = 0
	for (program, weight) in weightsOfSubTwrs:
		if weight in temp:
			balanced_weight = weight
			break
		else:
			temp.append(weight)
	
	for (program, weight) in weightsOfSubTwrs:
		if weight != balanced_weight:
			result = (program, balanced_weight - weight)
	
	if len(result) == 0:
		return result

	sub = findHighestUnbalance(weights, programs, result[0])

	if len(sub) == 0:
		return result
	else: return sub
		

def main():
	weights, programs = readInput('input')
	root = findroot(programs)
	print("root program: %s" % root)
	unbalance = findHighestUnbalance(weights, programs, root)
	print("correct weight for %s: %d" % (unbalance[0], (weights[unbalance[0]] + unbalance[1])))
	

if __name__ == "__main__":
	main()
