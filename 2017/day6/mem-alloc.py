#!/usr/bin/python3

def compare_int_lists(lista, listb):
    if (len(lista) != len(listb)):
        return False

    result = True
    length = len(lista)
    for i in range(length):
        if lista[i] != listb[i]:
            result = False
            break
    return result



def main():
# load inputdata from file
    with open('input', 'r') as inputfile:
        banks = []
        for line in inputfile:
            line = line.strip()
            for bank in line.split('\t'):
                banks.append(int(bank))

# debug
#    banks = [0, 2, 7, 0]

# loop detection
    looped_banks = []
    looped_banks.append(list(banks))
    loop = False
    cycles = 0
    while not (loop):
        # gather max value
        cycles = cycles + 1
        maxval = 0
        maxbank = 0
        for i in range (len(banks)):
            if banks[i] > maxval:
                maxval = banks[i]
                maxbank = i
#        print("banks:", banks)
#        print("maxbank = %d, maxval = %d" % (maxbank, maxval))

        # redistribute
        redist = banks[maxbank]
        i = maxbank
        banks[maxbank] = 0
        while redist > 0:
            i = i + 1
            banks[i % len(banks)] = banks[i % len(banks)] + 1
            redist = redist -1
        
#        print("redistributed banks:", banks)
        
        # check for loop:
        for i in range(len(looped_banks)):
            if compare_int_lists(looped_banks[i], banks):
                loop = True
                break
        
        looped_banks.append(list(banks))
        if cycles % 25 == 0:
            print("cycles: %d" %cycles)
#            break

    print("cycles until looped: %d" % cycles)
    print("cycles until loop: %d" % (cycles -i))


if __name__ == "__main__":
    main()
