#! /usr/bin/env python3

import queue

import intcode

INPUTFILE = 'input'
INPUT = 0

def permute(element_list):
    if len(element_list) < 2:
        return [element_list]
    results = []
    for element in element_list:
        result = [element]
        new_element_list = element_list.copy()
        new_element_list.remove(element)
        new_lists = permute(new_element_list)
        for new_list in new_lists:
            result = [element]
            result.extend(new_list)
            results.append(result)
    return results

def main():
    # get input program
    input_file = open(INPUTFILE, 'r')
    line = input_file.readline().strip()
    input_file.close()
    # set phases
    #phases = [0, 1, 2, 3, 4]
    #max_output = 0
    #best_list = []
    #for phase_list in permute(phases):
    #    phase_a = phase_list[0]
    #    phase_b = phase_list[1]
    #    phase_c = phase_list[2]
    #    phase_d = phase_list[3]
    #    phase_e = phase_list[4]
    #    # run the five amplifiers with the given phase settings
    #    inputs_a = [phase_a, INPUT]
    #    memory_a = list(map(int, line.split(',')))
    #    inputs_b = [phase_b, intcode.calculate(memory_a, inputs_a)]
    #    memory_b = list(map(int, line.split(',')))
    #    inputs_c = [phase_c, intcode.calculate(memory_b, inputs_b)]
    #    memory_c = list(map(int, line.split(',')))
    #    inputs_d = [phase_d, intcode.calculate(memory_c, inputs_c)]
    #    memory_d = list(map(int, line.split(',')))
    #    inputs_e = [phase_e, intcode.calculate(memory_d, inputs_d)]
    #    memory_e = list(map(int, line.split(',')))
    #    output = intcode.calculate(memory_e, inputs_e)
    #    if output > max_output:
    #        max_output = output
    #        best_list = phase_list
    #print("Max output (Part 1):", max_output)

    # set phases
    phases = [5, 6, 7, 8, 9]
    max_output = 0
    for phase_list in permute(phases):
        phase_a = phase_list[0]
        phase_b = phase_list[1]
        phase_c = phase_list[2]
        phase_d = phase_list[3]
        phase_e = phase_list[4]
        # run the five amplifiers with the given phase settings
        inputs_a = queue.Queue()
        inputs_a.put(phase_a)
        inputs_a.put(INPUT)
        memory_a = list(map(int, line.split(',')))
        inputs_b = queue.Queue()
        inputs_b.put(phase_b)
        memory_b = list(map(int, line.split(',')))
        inputs_c = queue.Queue()
        inputs_c.put(phase_c)
        memory_c = list(map(int, line.split(',')))
        inputs_d = queue.Queue()
        inputs_d.put(phase_d)
        memory_d = list(map(int, line.split(',')))
        inputs_e = queue.Queue()
        inputs_e.put(phase_e)
        memory_e = list(map(int, line.split(',')))
        # initialize amplifiers
        amp_a = intcode.Computer(memory_a, inputs_a, inputs_b)
        amp_b = intcode.Computer(memory_b, inputs_b, inputs_c)
        amp_c = intcode.Computer(memory_c, inputs_c, inputs_d)
        amp_d = intcode.Computer(memory_d, inputs_d, inputs_e)
        amp_e = intcode.Computer(memory_e, inputs_e, inputs_a)
        # start amplifier computers
        amp_a.start()
        amp_b.start()
        amp_c.start()
        amp_d.start()
        amp_e.start()
        # wait for computation to finish
        amp_a.join()
        amp_b.join()
        amp_c.join()
        amp_d.join()
        amp_e.join()
        # last input should be where amp_e puts it: in inputs_a
        output = inputs_a.get()
        #print("DEBUG output:", output)
        #print("DEBUG qsize of inputs_a:", inputs_a.qsize())
        if output > max_output:
            max_output = output
    print("Max output (Part 2):", max_output)

if __name__ == "__main__":
    main()
