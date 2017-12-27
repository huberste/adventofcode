#!/usr/bin/python3

def getInput(input):
	result = ""
	with open(input, "r") as inputfile:
		for line in inputfile:
			result = result + line.strip()
	return result

# a group is the tuple of the string of the group and it's score, e.g. ("{}", 1)
def getGroups(input):
	result = []
	groups = []
	garbage = False
	canceled = False
	garbageCounter = 0
	for i in range(len(input)):
		char = input[i]
		# new group starts
		if (char == '{') and not garbage:
			#new group opens
			groups.append(i)
		elif (char == '}') and not garbage:
			# innermost group closes
			groupstart = groups.pop()
			newgroup = (input[groupstart : i+1], 1+len(groups))
			result.append(newgroup)
		elif (char == '<') and not garbage:
			# garbage following!
			garbage = True
		elif (char == '>') and garbage:
			# probably closes garbage, except if canceled:
			if not canceled:
				#garbage closes
				garbage = False
			else:
				canceled = False
		elif (char == '!') and garbage:
			canceled = not canceled
		elif garbage and canceled:
			canceled = False
		elif garbage:
			garbageCounter = garbageCounter + 1
	print("garbage: %d" % garbageCounter)
	
	return result

def getScore(input):
	result = 0
	groups = getGroups(input)
	for group in groups:
		result = result + group[1]
	return result

def main():
	input = getInput("input")
	
	score = getScore(input)

	print("total score: %d" % score)
	

if __name__ == "__main__":
	main()
