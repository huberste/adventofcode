#!/usr/bin/python3

# stefan (dot) huber (at) stusta (dot) de
# http://adventofcode.com/2017/day/10

def getInput(input):
	result = ""
	with open(input, 'r') as inputfile:
		for line in inputfile:
			result = result + line.strip()
	return result

def inputPart1(inpt):
	result = []
	for number in inpt.split(','):
		result.append(int(number))
	return result

def inputPart2(inpt):
	result = []
	for char in inpt:
		result.append(ord(char))
	# now add fixed lengths to the sequence
	for number in [17, 31, 73, 47, 23]:
		result.append(number)
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

# to check the process, you can multiply the first tho numbers.
def hashPart1(lst):
	return lst[0] * lst[1]

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

def main():
	inpt = getInput("input")
	inptPart1 = inputPart1(inpt)
	sparse_hash = sparseHash(256, inptPart1, 1)
	print("knot hash for part 1:", hashPart1(sparse_hash))

	inptPart2 = inputPart2(inpt)
	sparse_hash = sparseHash(256, inptPart2, 64)
	dense_hash =  densifyHash(sparse_hash, 16)
	hash_representation = hexOfHash(dense_hash)
	print("knot hash for part 2: %s"% hash_representation)

if __name__ == "__main__":
	main()
