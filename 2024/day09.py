#! /usr/bin/env python3
"""Module for solving advent of code 2024/09"""

INPUT = "day09.input"

def fs_checksum(fs):
    """calculates the file system checksum"""
    result = 0
    for i, block in enumerate(fs):
        if block == ".":
            continue
        result += i * block
    return result

def extend_diskmap(diskmap):
    """extends a given diskman to the full file system"""
    fs = []
    file_id = 0
    file = True
    for block_len in diskmap:
        if file:
            fs.extend([file_id] * block_len)
            file_id += 1
        else:
            fs.extend(["."] * block_len)
        file = not file
    return fs

def stupid_defrag(fs):
    """defrags the file system, stupid way"""
    last_file_index = len(fs) - 1
    first_free_index = 0
    while True:
        while fs[last_file_index] == ".":
            last_file_index -= 1
        while fs[first_free_index] != ".":
            first_free_index += 1
        if last_file_index < first_free_index:
            break
        fs[first_free_index] = fs[last_file_index]
        fs[last_file_index] = "."
    return fs

def defrag_whole_files(fs):
    """defrags the file system, whole files moving now"""
    # find start of last file
    file_id = fs[-1]
    file_index = fs.index(file_id)
    free_index = fs.index(".")
    while file_index > free_index:
        file_len = fs.count(file_id)
        free_len = 1
        moved = False
        free_index = fs.index(".")
        # check if free space is large enough
        while not moved and file_index > free_index:
            free_len = 0
            while fs[free_index + free_len] == ".":
                free_len += 1
                if free_len >= file_len:
                    # move file
                    for i in range(file_len):
                        fs[free_index + i] = file_id
                        fs[file_index + i] = "."
                        moved = True
                    break
            if not moved:
                # find next free space
                free_index = fs.index(".", free_index + free_len)
                free_len = 0
        file_id -= 1
        file_index = fs.index(file_id)
        free_index = fs.index(".")
    return fs

def print_fs(fs):
    """nicely print a file system as in the instruction"""
    for block in fs:
        if isinstance(block, str):
            print(block, end='')
        else:
            print(block, end='')
    print()

def main():
    """It's the main function. Call with ./day09.py"""
    diskmap = None
    with open(INPUT, 'r', encoding='utf-8') as inputfile:
        diskmap = list(map(int, list(inputfile.read().strip())))
    fs = extend_diskmap(diskmap)
    fs = stupid_defrag(fs)
    part_one = fs_checksum(fs)
    print(f"file system checksum after block defrag: {part_one}")
    fs = extend_diskmap(diskmap)
    fs = defrag_whole_files(fs)
    part_two = fs_checksum(fs)
    print(f"file system checksum after file defrag: {part_two}")

if __name__ == "__main__":
    main()
