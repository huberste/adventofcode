#! /usr/bin/env python3
"""Module for solving advent of code 2024/05"""

def is_update_in_correct_order(update, rules):
    """check if the update is already in the right order"""
    for (index, number) in enumerate(update):
        for i in range(index):
            if not number in rules:
                continue
            if update[i] in rules[number]:
                return False
    return True

def sort_update(update, rules):
    """recursivley (if needed) sort the update"""
    sorted_update = []
    for (index, number) in enumerate(update):
        sorted_update.append(number)
        for i in range(index):
            if not number in rules:
                continue
            if update[i] in rules[number]:
                # this is wrongly sorted
                # swap
                tmp = sorted_update[i]
                sorted_update[i] = number
                sorted_update[index] = tmp
                break
    if is_update_in_correct_order(sorted_update, rules):
        return sorted_update
    return sort_update(sorted_update, rules)

def main():
    """It's the main function. Call with ./day05.py"""
    rules = {}
    updates = []
    section = 0
    with open('day05.input', 'r', encoding='utf-8') as inputfile:
        for line in inputfile:
            line = line.strip()
            if line == "":
                section += 1
                continue
            if section == 0:
                rule = list(map(int, line.split("|")))
                if rule[0] in rules:
                    rules[rule[0]].append(rule[1])
                else:
                    rules[rule[0]] = [rule[1]]
            elif section == 1:
                updates.append(list(map(int, line.split(","))))
    part_one = 0
    part_two = 0
    for update in updates:
        if is_update_in_correct_order(update, rules):
            part_one += update[int(len(update)/2)]
        else:
            sorted_update = sort_update(update, rules)
            part_two += sorted_update[int(len(update)/2)]
    print(f"correctly ordered updates: {part_one}")
    print(f"sorted updates: {part_two}")

if __name__ == "__main__":
    main()
