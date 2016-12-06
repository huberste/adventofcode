#!/usr/bin/python3

# Python3 script to solve part two of day 1 of the
# AdventOfCode 2016
# http://adventofcode.com/
#
# author Alexandra Meyer

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
#distances = {"0":0, "1":0, "2":0, "3":0}
pois=[]

pois.append("0,0")
#pois.append(str(x) + "," + str(y))
x=0
y=0

end = False

for direction in directions:
	if (end):
		break
	if (direction[0] == "R"):
		facing = (facing + 1) % 4 
	else:
		facing = (facing -1) % 4

	if (facing % 2 ==0):	
		#way = 1 für Norden, way = -1 für Süden
		way = -facing + 1
		for i in range (0,int(direction[1:])):
			y += way
			if ((str(x) + "," + str(y)) in pois):
				print("Gefunden:" + (str(x) + "," + str(y)))
				end = True
				break
			else:
				pois.append(str(x) + "," + str(y))

	else:
		#way = 1 für Ost, way = -1 für West
		way = -facing +2
		for i in range (0,int(direction[1:])):
			x += way
			if ((str(x) + "," + str(y)) in pois):
				print("Gefunden:" + (str(x) + "," + str(y)))
				end = True
				break
			else:
				pois.append(str(x) + "," + str(y))
		
print("Solution part 2:" + str(x+y)) 

#	distances[str(facing)]=distances[str(facing)]+int(direction[1:])		
#print(distances)

#sol= abs(distances["0"]-distances["2"]) + abs(distances["1"] - distances["3"])
#print("Solution:" + str(sol))


