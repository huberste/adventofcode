#!/usr/bin/python3

def getInput(inputfile):
	result = []
	with open(inputfile, 'r') as infile:
		for line in infile:
			result.append(line)
	return result



def main():
	maze = getInput("input")
	# search entry point
	posx = 0
	posy = 0
	direction = 2 # 0 = N 1 = E 2 = S 3 = W
	for char in maze[0]:
		if char == "|":
			break
		posx = posx + 1
	# follow the path
	run = True
	path = ""
	steps = 0
	while run:
		if (posy < 0) or (posy > len(maze) - 1):
			run = False
			break
		if (posx < 0) or (posx > len(maze[posy]) - 1):
			run = False
			break
		char = maze[posy][posx]
		if char == '+':
			# change direction...
			if (direction != 2) and (posy > 0):
				if maze[posy-1][posx] != ' ':
					direction = 0
					posy = posy - 1
					steps = steps + 1
					continue
			if (direction != 3) and (posx > 0):
				if maze[posy][posx+1] != ' ':
					direction = 1
					posx = posx + 1
					steps = steps + 1
					continue
			if (direction != 0) and (posy < len(maze)-1):
				if maze[posy+1][posx] != ' ':
					direction = 2
					posy = posy + 1
					steps = steps + 1
					continue
			if (direction != 1) and (posx < len(maze[posy])-1):
				if maze[posy][posx-1] != ' ':
					direction = 3
		# go into direction:
		if direction == 0:
			posy = posy - 1
			steps = steps + 1
		elif direction == 1:
			posx = posx + 1
			steps = steps + 1
		elif direction == 2:
			posy = posy + 1
			steps = steps + 1
		elif direction == 3:
			posx = posx - 1
			steps = steps + 1
		if not char in ("|-+ "):
			path = path + char
		if char == ' ':
			run = False
	print("Path:", path)
	print("Steps: %d" % (steps - 1))


if __name__ == "__main__":
	main()
