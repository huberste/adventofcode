#!/usr/bin/python3

# the spiral memory has 1 in the middle,
# then it goes to the right and counter-clockwise for each following number:
# 17 16 15 14 13
# 18  5  4  3 12
# 19  6  1  2 11
# 20  7  8  9 10
# 21 22 23 24 25 ...

input = 325489

# part 1
# output: Manhattan-Distance from input to 1

# nth_odd_numer = 2n-1
# square_of_nth_odd_number = (2n-1)*(2n-1)
# square_of_nth_odd_number is always bottom right of the spiral memory.

# first we look which odd square number is the next eqal-or-larger:

ring = 0
square = 0
while (square < input): 
	ring = ring + 1
	square = (2*ring-1)*(2*ring-1)
	
print("the number is in the %dth ring" % ring)

# the nth ring has (2n-1) spaces in each direction.
# we now check on which quarter of the ring we are:

# the calculated square number is on the bottom right of the ring.
bottom_right = square
print("bottom_right: %d" % bottom_right)
if input == bottom_right:
	print("input is bottom_right.")
	print("manhattan-distance to 1: %d" % (ring-1 +  ring-1))

# if we subtract (2n-1) - 1 from bottom_right, we go to bottom_left:
bottom_left = bottom_right - ((2*ring) - 2)
print("bottom_left: %d" % bottom_left)
if input == bottom_left:
	print("input is bottom_left.")
	print("manhattan-distance to 1: %d" % (ring-1 +  ring-1))

# let's check, if the input is on the bottom row:
if input > bottom_left:
	print("input is in bottom row.")
	mid = bottom_left + ring - 1
	distance_to_mid = input - mid
	if distance_to_mid < 0:
		distance_to_mid = -distance_to_mid
	distance = (ring-1) + distance_to_mid
	print("manhattan-distance to 1: %d" % distance)


# if we subtract (2n-1) - 1 from bottom_left, we go to top_left:
top_left = bottom_left - ((2*ring) - 2)
print("top_left: %d" % top_left)
if input == top_left:
	print("input is top_left.")
	print("manhattan-distance to 1: %d" % (ring-1 +  ring-1))

# let's check, if the input is on the left column:
if input > top_left:
	print("input is in left column.")
	mid = top_left + ring - 1
	distance_to_mid = input - mid
	if distance_to_mid < 0:
		distance_to_mid = -distance_to_mid
	distance = (ring-1) + distance_to_mid
	print("manhattan-distance to 1: %d" % distance)
	ecit(0)

# if we subtract (2n-1) - 1 from top_left, we go to top_right:
top_right = top_left - ((2*ring) - 2)
print("top_right: %d" % top_right)
if input == top_right:
	print("input is top_right.")
	print("manhattan-distance to 1: %d" % (ring-1 +  ring-1))

# let's check, if the input is on the top row:
if input > top_right:
	print("input is in top row.")
	mid = top_right + ring - 1
	distance_to_mid = input - mid
	if distance_to_mid < 0:
		distance_to_mid = -distance_to_mid
	distance = (ring-1) + distance_to_mid
	print("manhattan-distance to 1: %d" % distance)

# nothing else is the case:
# input is on the right column
print("input is in right column.")
mid = top_right - (ring - 1)
distance_to_mid = input - mid
if distance_to_mid < 0:
	distance_to_mid = -distance_to_mid
distance = (ring-1) + distance_to_mid
print("manhattan-distance to 1: %d" % distance)

# part 2:
# As a stress test on the system, the programs here clear the grid and then store the value 1 in square 1. Then, in the same allocation order as shown above, they store the sum of the values in all adjacent squares, including diagonals.
# output: first value written > input


