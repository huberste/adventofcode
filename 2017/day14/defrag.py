#!/usr/bin/python3

import sys

def getInput(inputfile):
    result = ""
    with open(inputfile, 'r') as input:
        for line in input:
            result = result + line.strip()
    return result

def reverseSublist(lst, start, end):
	for i in range(int((end - start + 1)/2)):
		tmp = lst[(start + i) % len(lst)]
		lst[(start + i) % len(lst)] = lst[(end - i) % len(lst)]
		lst[(end - i) % len(lst)] = tmp
	return lst

def sparseHash(size, lengths, rounds):
	pos = 0 # current pointer position
	skipSize = 0 # current skipSize
	result = 0 # result is numbers[0] * numbers[1]
	numbers = [] # list of numbers
	for i in range(size):
		numbers.append(i)
	for j in range(rounds):
		for i in range(len(lengths)):
			length = lengths[i]
			# reverse numbers[pos:pos+length]
			start = pos
			end = (pos + length - 1)
			numbers = reverseSublist(numbers, start, end)
			pos = pos + length + skipSize
			skipSize = skipSize + 1
	return numbers

def knotHashInput(inpt):
	result = []
	for char in inpt:
		result.append(ord(char))
	# now add fixed lengths to the sequence
	for number in [17, 31, 73, 47, 23]:
		result.append(number)
	return result

# Once the rounds are complete, you will be left with the numbers from 0 to 255
# in some order, called the sparse hash. Your next task is to reduce these to a
# list of only 16 numbers called the dense hash. To do this, use numeric
# bitwise XOR to combine each consecutive block of 16 numbers in the sparse
# hash (there are 16 such blocks in a list of 256 numbers). So, the first
# element in the dense hash is the first sixteen elements of the sparse hash
# XOR'd together, the second element in the dense hash is the second sixteen
# elements of the sparse hash XOR'd together, etc.
def densifyHash(sparse_hash, factor):
	result = []
	for i in range(int(len(sparse_hash) / factor)):
		tmp = 0
		for j in range(factor):
			if j == 0:
				tmp = sparse_hash[(i*factor)+j]
			else:
				tmp = tmp ^ sparse_hash[(i*factor)+j]
		result.append(tmp)
	return result

def hexOfHash(dense_hash):
	result = ""
	for i in range(len(dense_hash)):
		number = dense_hash[i]
		result = result + ("%0.2x"  % number)
	return result

def knothash(arg):
    inpt = knotHashInput(arg)
    sparse_hash = sparseHash(256, inpt, 64)
    dense_hash =  densifyHash(sparse_hash, 16)
    hash_representation = hexOfHash(dense_hash)
    return hash_representation

def knotHashToBinaryString(hashValue):
    result = bin(int(hashValue, 16))[2:].zfill(128)
    return result

def connect(pos, defragmap, regionmap, region):
    x, y = pos[0], pos[1]
    regionmap[y][x] = region
    # left:
    if x > 0:
        if (defragmap[y][x-1] == "1") and (regionmap[y][x-1] < 0):
            connect((x-1, y), defragmap, regionmap, region)
    # right:
    if x < 127:
        if (defragmap[y][x+1] == "1") and (regionmap[y][x+1] < 0):
            connect((x+1, y), defragmap, regionmap, region)
    # up:
    if y > 0:
        if (defragmap[y-1][x] == "1") and (regionmap[y-1][x] < 0):
            connect((x, y-1), defragmap, regionmap, region)
    # down:
    if y < 127:
        if (defragmap[y+1][x] == "1") and (regionmap[y+1][x] < 0):
            connect((x, y+1), defragmap, regionmap, region)

    return regionmap

def getNumOfRegions(defragmap):
    # regionmap is a list of lists.
    # each list in the list is one line of the defragmap,
    # and each char in the list is the region of the space in the defragmap
    regionmap = []
    for y in range(len(defragmap)):
        append = []
        for x in range(len(defragmap[y])):
            append.append(-1)
        regionmap.append(append)
    region = 0
    pos = (0,0)
    for y in range(len(defragmap)):
        for x in range(len(defragmap[y])):
            if defragmap[y][x] == "0":
                regionmap[y][x] = 0
            elif regionmap[y][x] < 0:
                region = region + 1
                regionmap = connect((x,y), defragmap, regionmap, region)
    return region

def main(args):
    if len(args) < 2:
        return 1;
    key = getInput(args[1])
    defragmap = []
    for i in range(128):
        defragmap.append(knotHashToBinaryString(knothash(key+("-%d" %i))))
    ctr = 0
    for line in defragmap:
        for char in line:
            if char == "1":
                ctr = ctr + 1
    print("used squares: %d" % ctr)
    print("Number of regions in defragmap: %d" % getNumOfRegions(defragmap))

if __name__ == "__main__":
    args = sys.argv
    main(args)
#    print(bin(int("1111", 16))[2:].zfill(128))
