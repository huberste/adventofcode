#!/usr/bin/python3

import sys;

def main():
    valid_passphrases_part_1 = 0
    valid_passphrases_part_2 = 0
    with open('input', 'r') as inputfile:
        for line in inputfile:
            line=line.strip()
            words_part_1 = {}
            words_part_2 = {}
            valid_part_1 = True
            valid_part_2 = True
            for word in line.split():
                if word in words_part_1:
                    valid_part_1 = False;
                else:
                    words_part_1[word] = True
                sorted_word = ''.join(sorted(word))
                if sorted_word in words_part_2:
                    valid_part_2 = False;
                else:
                    words_part_2[sorted_word] = True
                    
            if valid_part_1 == True:
                valid_passphrases_part_1 = valid_passphrases_part_1 + 1
            
            if valid_part_2 == True:
                valid_passphrases_part_2 = valid_passphrases_part_2 + 1
                

    print("valid passphrases part 1: %d" % valid_passphrases_part_1)
    print("valid passphrases part 2: %d" % valid_passphrases_part_2)

if __name__ == "__main__":
        main()
