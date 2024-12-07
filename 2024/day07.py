#! /usr/bin/env python3
"""Module for solving advent of code 2024/07"""

import re

INPUT = "day07.input"

def solve_equation_with(equation, op, part):
    new_equation = equation.copy()
    if op == "+":
        new_equation[1] = new_equation[1] + new_equation[2]
    elif op == "*":
        new_equation[1] = new_equation[1] * new_equation[2]
    elif op == "||":
        new_equation[1] = int(str(new_equation[1]) + str(new_equation[2]))
    else:
        raise Exception(f"Oh no, I don't know operation '{op}'")
    del new_equation[2]
    if len(new_equation) > 2:
        if part == 1:
            return (solve_equation_with(new_equation, "+", 1) or solve_equation_with(new_equation, "*", 1))
        if part == 2:
            return (solve_equation_with(new_equation, "+", 2) or solve_equation_with(new_equation, "*", 2) or solve_equation_with(new_equation, "||", 2))
    else:
        if new_equation[0] == new_equation[1]:
            return True
    return False

def solve_equation_pt_one(equation):
    """"""
    return (solve_equation_with(equation, "+", 1) or solve_equation_with(equation, "*", 1))

def solve_equation_pt_two(equation):
    """"""
    return (solve_equation_with(equation, "+", 2) or solve_equation_with(equation, "*", 2) or solve_equation_with(equation, "||", 2))

def main():
    """It's the main function. Call with ./day07.py"""
    equations = []
    with open(INPUT, 'r', encoding='utf-8') as inputfile:
        for line in inputfile:
            equations.append(line.strip())
    part_one = 0
    part_two = 0
    for equation in equations:
        eq = re.findall(r'\d+', equation)
        eq = list(map(int, eq))
        if solve_equation_pt_one(eq):
            part_one += eq[0]
        if solve_equation_pt_two(eq):
            part_two += eq[0]

    print(f"total calibration result: {part_one}")
    print(f"those damn elefants: {part_two}")

if __name__ == "__main__":
    main()
