#! /usr/bin/env python3

###
# Part 1:
# However, they do remember a few key facts about the password:
# - It is a six-digit number.
# - The value is within the range given in your puzzle input.
# - Two adjacent digits are the same (like 22 in 122345).
# - Going from left to right, the digits never decrease; they only ever increase or stay the same (like 111123 or 135679).
### Part 2 additionally:
# - the two adjacent matching digits are not part of a larger group of matching digits.


INPUTFILE = 'input'
DIGITS = 6

def main():
    # read initial memory from input file
    input_file = open(INPUTFILE, 'r')
    (start, stop) = map(int, input_file.readline().strip().split('-'))
    input_file.close()
    print (start, "-", stop)
    passwords = [] # save all good passwords here
    passwords_two = [] # save all good passwords here (part 2)
    for number in range(start, stop+1, 1):
        if number % 10000 == 0:
            print("\r[PROGRESS]", number, end="")
        last_digit = -1
        adjacent = False
        matching = 1
        matching_two = False
        for power in range(DIGITS, 0, -1):
            digit = int(number / (10 ** (power-1)) % 10)
            if (digit < last_digit):
                adjacent = False
                break # next number
            elif (digit == last_digit):
                adjacent = True
                matching += 1
            else:
                if matching == 2:
                    matching_two = True
                matching = 1
                last_digit = digit
        if adjacent:
            #print ("[DEBUG] found valid password:", number)
            passwords.append(number)
            if matching_two or (matching == 2):
                passwords_two.append(number)

    print("\rFound", len(passwords), "valid passwords (part 1).")
    print("Found", len(passwords_two), "valid passwords (part 2).")

if __name__ == "__main__":
    main()
