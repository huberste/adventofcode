#! /usr/bin/env python3
"""Module for solving advent of code 2024/11"""

INPUT = "day11.input"

stonemap = {}

def get_number_of_stones_after(stone, blinks):
    result = 1
    if not stone in stonemap:
        stonemap[stone] = {}
    if stone in stonemap:
        if blinks in stonemap[stone]:
            return stonemap[stone][blinks]
    if blinks == 0:
        result = 1
    elif stone == 0:
        result = get_number_of_stones_after(1, blinks-1)
    else:
        number = str(stone)
        if len(number) % 2 == 0:
            result = get_number_of_stones_after(int(number[:int(len(number)/2)]), blinks - 1)
            result += get_number_of_stones_after(int(number[int(len(number)/2):]), blinks - 1)
        else:
            result = get_number_of_stones_after(stone * 2024, blinks - 1)
    stonemap[stone][blinks] = result
    return result

def blink(stones):
    """this function blinks() once. Don't use this except for single blinks. It ca take a whole lot of time!"""
    i = 0
    target = len(stones)
    while i < target:
        # If the stone is engraved with the number 0, it is replaced by a stone engraved with the number 1.
        if stones[i] == 0:
            stones[i] = 1
        elif len(str(stones[i])) % 2 == 0:
            # If the stone is engraved with a number that has an even number of digits, it is replaced by two stones. The left half of the digits are engraved on the new left stone, and the right half of the digits are engraved on the new right stone. (The new numbers don't keep extra leading zeroes: 1000 would become stones 10 and 0.)
            number = str(stones[i])
            stones[i] = int(number[:int(len(number)/2)])
            # we can ignore the ordering, so new stones will be put at the end. This makes stuff faster (but still not fast enough)
            stones.append(int(number[int(len(number)/2):]))
        else:
            # If none of the other rules apply, the stone is replaced by a new stone; the old stone's number multiplied by 2024 is engraved on the new stone.
            stones[i] = stones[i] * 2024
        i += 1

def main():
    """It's the main function. Call with ./day10.py"""
    with open(INPUT, 'r', encoding='utf-8') as inputfile:
        stones = (list(map(int, inputfile.read().strip().split())))
    # i = 0
    # while i < 25:
    #     print(i)
    #     blink(stones)
    #     i += 1
    #     print(len(stones))
    # print(f"Stones after blinking 25 times: {len(stones)}")
    # while i < 75:
    #     print(i)
    #     blink(stones)
    #     i += 1
    #     print(len(stones))
    # print(f"Stones after blinking 75 times: {len(stones)}")
    # for the result, we can completely ignore ordering of the stones
    # so we will just have a look at each stone individually.
    # additionally we can buffer results for stones in the hashmap
    part_one = 0
    part_two = 0
    for stone in stones:
        part_one += get_number_of_stones_after(stone, 25)
        part_two += get_number_of_stones_after(stone, 75)
    #print (stonemap)
    print(f"Stones after blinking 25 times: {part_one}")
    print(f"Stones after blinking 75 times: {part_two}")

if __name__ == "__main__":
    main()
