#!/usr/bin/python3

# load inputdata from file
inputfile = open('input', 'r')
inputdata = inputfile.readline()
inputfile.close()

# Debug: print read stuff:
print("[DEBUG] read stuff = "+inputdata)

# get directions
directions = inputdata.split(', ')

print(directions[5][0] + directions[5][1:])

#Nord=0 Ost=1, Süd=2, West=3
facing = 0
distances = {"0":0, "1":0, "2":0, "3":0}

for direction in directions:
	if (direction[0] == "R"):
		facing = (facing + 1) % 4 
	else:
		facing = (facing -1) % 4
	
	distances[str(facing)]=distances[str(facing)]+int(direction[1:])

print(distances)

sol= abs(distances["0"]-distances["2"]) + abs(distances["1"] - distances["3"])
print("Solution:" + str(sol))
