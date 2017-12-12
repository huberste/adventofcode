#!/usr/bin/python3

def getInput(inputfile):
	result = {}
	with open(inputfile, 'r') as infile:
		for line in infile:
			splitline = line.strip().split(" <-> ")
			key = int(splitline[0])
			pipes = []
			for pipe in splitline[1].split(", "):
				pipes.append(int(pipe))
			result[key] = pipes
	return result

def getConnected(prog, pipes, connected):
	result = connected
	if not (prog in result):
		result.append(prog)
	for pipe in pipes[prog]:
		if not (pipe in result):
			newPipes = getConnected(pipe, pipes, result)
			for newPipe in newPipes:
				if not (newPipe in result):
					result.append(newPipe)
	return result

def getGroups(pipes):
	result = []
	for program in pipes:
		programInGroup = False
		for group in result:
			if program in group:
				programInGroup = True
				break
		if not programInGroup:
			result.append(getConnected(program, pipes, []))
	return result

def main():
	pipes = getInput("input")
	connectedPipes = getConnected(0, pipes, [])
	print("Programs connected to 0: %d" % len(connectedPipes))
	groups = getGroups(pipes)
	print("Total number of groups: %d" % len(groups))

if __name__ == "__main__":
	main()
