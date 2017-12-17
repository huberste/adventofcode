#!/usr/bin/python3

INPUT = 369
LAST_VALUE_WRITTEN_PART_1 = 2017
LAST_VALUE_WRITTEN = 50000000

def main(inpt):
	state = [ 0 ]
	pos = 0
	pos0 = 0 # this stays true all the time
	valueAfter0 = 0
	for i in range(1, LAST_VALUE_WRITTEN_PART_1 + 1):
		# step input steps
		pos = (pos + inpt) % i
		state.insert(pos + 1, i)
		pos = pos + 1
	print("Value after %d: %d" % (LAST_VALUE_WRITTEN_PART_1, state[(pos+1) % LAST_VALUE_WRITTEN]))

	state = [ 0 ]
	pos = 0
	for i in range(1, LAST_VALUE_WRITTEN + 1):
		pos = (pos + inpt) % i
		if pos == 0:
			valueAfter0 = i
		pos = pos + 1

	print("Value after %d iterations after value 0: %d" % (LAST_VALUE_WRITTEN, valueAfter0))

if __name__ == "__main__":
	main(INPUT)
