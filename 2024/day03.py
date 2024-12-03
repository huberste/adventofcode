#! /usr/bin/env python3

import re

def main():
    memory = None
    with open('day03.input', 'r', encoding='utf-8') as inputfile:
        memory = inputfile.read()
    part_one = 0
    part_two = 0
    do = True
    instructions = re.findall(r'mul\(\d+,\d+\)|do\(\)|don\'t\(\)', memory)
    for instruction in instructions:
        if instruction.startswith("mul"):
            nums = re.findall(r'\d+', instruction)
            result = int(nums[0]) * int(nums[1])
            part_one += result
            if do:
                part_two += result
        elif instruction == "do()":
            do = True
        elif instruction == "don't()":
            do = False
    print(f"added up mul results: {part_one}")
    print(f"added up enabled mul results: {part_two}")

if __name__ == "__main__":
    main()
