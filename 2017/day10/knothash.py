#!/usr/bin/python3

def getInput(input):
	result = []
	with open(input, 'r') as inputfile:
		for line in inputfile:
			result.extend(line.strip().split(','))
	result = list(map(int, result))
	return result

def reverseSublist(lst, start, end):
	print("reversesublist", lst, start, end)
	for i in range((end - start + 1)/2):
		tmp = lst[(start + i) % len(lst)]
		lst[(start + i) % len(lst)] = lst[(end - i) % len(lst)]
		lst[(end - i) % len(lst)] = tmp
	return lst

def knothash(size, lengths):
	pos = 0 # current pointer position
	skipSize = 0 # current skipSize
	result = 0 # result is numbers[0] * numbers[1]
	numbers = [] # list of numbers
	for i in range(size):
		numbers.append(i)
	print(numbers)
	for i in range(len(lengths)):
		length = lengths[i]
		# reverse numbers[pos:pos+length]
		start = pos
		end = (pos + length - 1)
		numbers = reverseSublist(numbers, start, end)
		print(numbers)
		pos = pos + length + skipSize
		skipSize = skipSize + 1
	result = numbers[0] * numbers[1]
	return result

def main():
	input = getInput("input")
	print(input)
	hash = knothash(256, input)
	print("hash: %d" % hash)
	

if __name__ == "__main__":
	main()
