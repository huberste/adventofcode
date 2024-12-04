#! /usr/bin/env python3
"""Module for solving advent of code 2024/04"""

RIGHT = 1
LEFT = -1
UP = -1
DOWN = 1
STRAIGHT = 0

def is_word_at(word, lines, row, col, rowdir, coldir):
    """Function checks if the word is at (row,col) starting in  given direction"""
    for letter in word[1:]:
        row += rowdir
        col += coldir
        if row < 0 or row >= len(lines) or col < 0 or col >= len(lines[row]):
            return False
        if lines[row][col] != letter:
            return False
    return True

def count_all_word(word, lines):
    """Function finds and counts all occurences of the given word"""
    result = 0
    for row, line in enumerate(lines):
        for col, letter in enumerate(line):
            if letter == word[0]:
                for (rowdir, coldir) in [
                    (STRAIGHT, RIGHT),
                    (DOWN, RIGHT),
                    (DOWN, STRAIGHT),
                    (DOWN, LEFT),
                    (STRAIGHT, LEFT),
                    (UP, LEFT),
                    (UP, STRAIGHT),
                    (UP, RIGHT)]:
                    if is_word_at(word, lines, row, col, rowdir, coldir):
                        result += 1
    return result

def is_x_mas_at(lines, row, col):
    """Function to check if there's an X-MAS at (row, col)"""
    if row < 1 or row >= len(lines) - 1 or col < 1 or col >= len(lines[row]) - 1:
        return False
    upleft    = lines[row + UP  ][col + LEFT ]
    downright = lines[row + DOWN][col + RIGHT]
    upright   = lines[row + UP  ][col + RIGHT]
    downleft  = lines[row + DOWN][col + LEFT ]
    if all([upleft  in "MS",
            downright in "MS",
            upleft  != downright,
            upright in "MS",
            downleft in "MS",
            upright != downleft]):
        return True
    return False

def count_all_x_mas(lines):
    """Function to find and count all occurences of an X-MAS"""
    result = 0
    for row, line in enumerate(lines):
        for col, letter in enumerate(line):
            if letter == "A":
                if is_x_mas_at(lines, row, col):
                    result += 1
    return result

def main():
    """It's the main function. Call with ./day04.py"""
    lines = []
    with open('day04.input', 'r', encoding='utf-8') as inputfile:
        for line in inputfile:
            lines.append(list(line.strip()))
    part_one = 0
    part_two = 0
    word = list("XMAS")
    part_one += count_all_word(word, lines)
    part_two += count_all_x_mas(lines)
    print(f"XMAS in word search: {part_one}")
    print(f"X-MAS in word search: {part_two}")

if __name__ == "__main__":
    main()
