#!/usr/bin/python3

# load inputdata from file
inputfile = open('input', 'r')
inputdata = inputfile.readline()
inputfile.close()

# Debug: print read stuff:
#print("[DEBUG] read stuff = "+inputdata)

# get directions
directions = inputdata.split(', ')

# directions: N,E,S,W = 0,1,2,3
facing = 0

pois = []

x = 0;
y = 0;

for direction in directions:
	x_before = x
	y_before = y
	
	turn = direction[0]
	#print("[DEBUG] direction = " + turn)
	length = int(direction[1:])
	#print("[DEBUG] length = " + str(length))
	if (turn == 'L'):
		facing = (facing+3) % 4
	else: # direction = 'R'
		facing = (facing + 1) % 4

	if (facing == 0):
		x += length
	elif (facing == 1):
		y += length
	elif (facing == 2):
		x -= length
	elif (facing == 3):
		y -= length
	
	last_poi_x = 0
	last_poi_y = 0
	
	for poi in pois:
		poi_x = int(poi.split(',')[0])
		poi_y = int(poi.split(',')[1])
		
		# collision?

		if (poi_x == last_poi_x):
			# [poi,last_poi] senkrecht
			if (x_before < x):
				if ((x_before <= poi_x) and (poi_x <= x)):
					#collision
					print()
			else:
				if ((x_before >= poi_x) and (poi_x >= x)):
					# collision
					print()
		else:
			# [poi,last_poi] waagerecht
			if (y_before < y):
				if ((y_before <= poi_y) and (poi_y <= y)):
					#collision
					print()
			else:
				if ((y_before >= poi_y) and (poi_y >= y)):
					# collision
					print()
		
		
		last_poi_x = poi_x
		last_poi_y = poi_y
	
	pois.append(str(x) + "," + str(y))
	
	
print("[DEBUG]" + str(pois))
	
#distance = abs(distance_N - distance_S) + abs(distance_E - distance_W)

#print (distance)
