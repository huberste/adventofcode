#!/usr/bin/python3

# the spiral memory has 1 in the middle,
# then it goes to the right and counter-clockwise for each following number:
# 17 16 15 14 13
# 18  5  4  3 12
# 19  6  1  2 11
# 20  7  8  9 10
# 21 22 23 24 25 ...

# nth_odd_numer = 2n-1
# square_of_nth_odd_number = (2n-1)*(2n-1)
# square_of_nth_odd_number is always bottom right of the spiral memory.

day_input = 325489

# part 1
# output: Manhattan-Distance from input to 1
def part1(input):
# first we look which odd square number is the next eqal-or-larger:
    ring = 0
    square = 0
    while (square < input): 
            ring = ring + 1
            square = (2*ring-1)*(2*ring-1)
            

# the nth ring has (2n-1) spaces in each direction.
# we now check on which quarter of the ring we are:

# the calculated square number is on the bottom right of the ring.
    bottom_right = square
    if input == bottom_right:
            print("manhattan-distance to 1: %d" % (ring-1 +  ring-1))
            return

# if we subtract (2n-1) - 1 from bottom_right, we go to bottom_left:
    bottom_left = bottom_right - ((2*ring) - 2)
    if input == bottom_left:
            print("manhattan-distance to 1: %d" % (ring-1 +  ring-1))
            return

# let's check, if the input is on the bottom row:
    if input > bottom_left:
            mid = bottom_left + ring - 1
            distance_to_mid = input - mid
            if distance_to_mid < 0:
                    distance_to_mid = -distance_to_mid
            distance = (ring-1) + distance_to_mid
            print("manhattan-distance to 1: %d" % distance)
            return

# if we subtract (2n-1) - 1 from bottom_left, we go to top_left:
    top_left = bottom_left - ((2*ring) - 2)
    if input == top_left:
            print("manhattan-distance to 1: %d" % (ring-1 +  ring-1))
            return

# let's check, if the input is on the left column:
    if input > top_left:
            mid = top_left + ring - 1
            distance_to_mid = input - mid
            if distance_to_mid < 0:
                    distance_to_mid = -distance_to_mid
            distance = (ring-1) + distance_to_mid
            print("manhattan-distance to 1: %d" % distance)
            return

# if we subtract (2n-1) - 1 from top_left, we go to top_right:
    top_right = top_left - ((2*ring) - 2)
    if input == top_right:
            print("manhattan-distance to 1: %d" % (ring-1 +  ring-1))
            return

# let's check, if the input is on the top row:
    if input > top_right:
            mid = top_right + ring - 1
            distance_to_mid = input - mid
            if distance_to_mid < 0:
                    distance_to_mid = -distance_to_mid
            distance = (ring-1) + distance_to_mid
            print("manhattan-distance to 1: %d" % distance)
            return

# nothing else is the case:
# input is on the right column
    mid = top_right - (ring - 1)
    distance_to_mid = input - mid
    if distance_to_mid < 0:
            distance_to_mid = -distance_to_mid
    distance = (ring-1) + distance_to_mid
    print("manhattan-distance to 1: %d" % distance)
    return

# part 2:
# As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.
# output: first value written > input

def ringoffield(field):
	result = 0
	square = 0
	while (square < field): 
		result = result + 1
		square = bottomright(result)
	return result

def bottomright(ring):
	result = (2*ring-1)*(2*ring-1)
	return result

def bottomleft(ring):
	return bottomright(ring) - (2*(ring-1))

def topleft(ring):
	return bottomleft(ring) - (2*(ring-1))

def topright(ring):
	return topleft(ring) - (2*(ring-1))

def isintoprow(field):
	ring = ringoffield(field)
	if (field < topleft(ring)) & (field > topright(ring)):	
		return True
	return False

def isinrightcol(field):
	ring = ringoffield(field)
	if (field < topright(ring)):
		return True
	return False

def isinbottomrow(field):
	ring = ringoffield(field)
	if (field < bottomright(ring)) & (field > bottomleft(ring)):	
		return True
	return False

def isinleftcol(field):
	ring = ringoffield(field)
	if (field < bottomleft(ring)) & (field > topleft(ring)):	
		return True
	return False

def left(field):
	ring = ringoffield(field)
	if isinleftcol(field) or (field == topleft(ring)) or (field == bottomleft(ring)):
		return field + (topleft(ring+1)-topleft(ring)) +1
	elif isintoprow(field) or (field == topright(ring)):
		return field+1
	elif isinbottomrow(field) or (field == bottomright(ring)):
		return field-1
        elif (field == bottomright(ring-1) +1):
                return field-1
	elif isinrightcol(field):
		return field - (topright(ring)-topright(ring-1) -1)
        # should never come here...
	return "There was an error in left(field)!"

def right(field):
	ring = ringoffield(field)
	if isinbottomrow(field) or (field == bottomright(ring)) or (field == bottomleft(ring)):
		return field+1
	elif isinrightcol(field) or (field == topright(ring)):
		return field + (topright(ring+1)-topright(ring) -1)
	elif isinleftcol(field):
		return field - (topleft(ring)-topleft(ring-1)+1) 
	elif isintoprow(field) or (field == topleft(ring)):
		return field-1
        # should never come here...
	return "There was an error in right(field)!"

def top(field):
	ring = ringoffield(field)
	if isintoprow(field) or (field == topleft(ring)) or (field == topright(ring)):
		return field + (topright(ring+1) - topright(ring) + 1)
	elif isinrightcol(field):
		return field + 1
	elif isinleftcol(field) or (field == bottomleft(ring)):
		return field - 1
	elif isinbottomrow(field) or (field == bottomright(ring)):
		return field - (bottomright(ring) - bottomright(ring-1) -1)
        # should never come here...
	return "There was an error in top(field)!"

def bottom(field):
	ring = ringoffield(field)
	if isinbottomrow(field) or (field == bottomright(ring)) or (field == bottomleft(ring)):
		return field + (bottomright(ring+1) - bottomright(ring) -1)
	elif isintoprow(field):
		return field - (topright(ring) - topright(ring-1) + 1)
        elif (field == bottomright(ring-1)+1) :
                return bottomright(ring)
	elif isinrightcol(field) or (field == topright(ring)):
		return field - 1
	elif isinleftcol(field) or (field == topleft(ring)):
		return field + 1
        # should never come here...
	return "There was an error in top(field)!"

def part2(input):
    value_written = 1

    #list of values
    values = [0, 1]
    field = 1
    value_written = 1
    while value_written <= input:
        field = field + 1
        value_written = 0
        if left(field) < field:
            value_written = value_written + values[left(field)]
        if left(top(field)) < field:
            value_written = value_written + values[left(top(field))]
        if top(field) < field:
            value_written = value_written + values[top(field)]
        if top(right(field)) < field:
            value_written = value_written + values[top(right(field))]
        if right(field) < field:
            value_written = value_written + values[right(field)]
        if bottom(right(field)) < field:
            value_written = value_written + values[bottom(right(field))]
        if bottom(field) < field:
            value_written = value_written + values[bottom(field)]
        if bottom(left(field)) < field:
            value_written = value_written + values[bottom(left(field))]
        values.append(value_written)

    print("value_written: %d" % value_written)
    
def main():
    part1(day_input)
    part2(day_input)

if __name__ == "__main__":
    main()
