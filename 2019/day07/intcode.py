"""Module intcode docstring:
The implementation of the intcode computer for the Advent of Code 2019
"""

from threading import Thread
import queue

class Computer(Thread):
    """The implementation of the intcode computer for the Advent of Code 2019
    Now it's a thread.
    """

    def __init__(self, program, inqueue, outqueue):
        """initialize a new intcode computer with the given prgram"""
        super().__init__()
        self.memory = program # memory of the intcode computer, list of integers
        self.inqueue = inqueue # where to get INPUT from
        self.outqueue = outqueue # where to save OUTPUT to

    def run(self):
        """starts the calculation"""
        instruction_pointer = 0
        output = -1
        running = True
        while running:
            operation = self.memory[instruction_pointer]
            opcode = operation % 100
            parameter_mode_one = int(operation /  100 % 10)
            #print("[DEBUG] param one mode:", parameter_mode_one)
            parameter_mode_two = int(operation / 1000 % 10)
            #print("[DEBUG] param two mode:", parameter_mode_two)
            parameter_mode_three = int(operation / 10000 % 10)
            #print("[DEBUG] param thr mode:", parameter_mode_three)
            #print("[DEBUG] opcode", opcode)
            if opcode == 1:
                # add
                param_one = self.memory[instruction_pointer+1]
                if parameter_mode_one == 0:
                    param_one = self.memory[param_one]
                param_two = self.memory[instruction_pointer+2]
                if parameter_mode_two == 0:
                    param_two = self.memory[param_two]
                param_three = self.memory[instruction_pointer+3]
                if parameter_mode_three == 0:
                    #param_three = memory[param_three]
                    pass
                else:
                    print("[WARN] parameter mode != 0 for ADD...")
                result = param_one + param_two
                #print("[DEBUG] ADD", param_one, "+", param_two, "to", param_three)
                self.memory[param_three] = result
                instruction_pointer += 4
            elif opcode == 2:
                # multiply
                param_one = self.memory[instruction_pointer+1]
                if parameter_mode_one == 0:
                    param_one = self.memory[param_one]
                param_two = self.memory[instruction_pointer+2]
                if parameter_mode_two == 0:
                    param_two = self.memory[param_two]
                param_three = self.memory[instruction_pointer+3]
                if parameter_mode_three == 0:
                    #param_three = memory[param_three]
                    pass
                else:
                    print("[WARN] parameter mode != 0 for MUL...")
                result = param_one * param_two
                #print("[DEBUG] MUL", param_one, "*", param_two, "to", param_three)
                self.memory[param_three] = result
                instruction_pointer += 4
            elif opcode == 3:
                # INPUT
                param_one = self.memory[instruction_pointer+1]
                if parameter_mode_one == 0:
                    #param_one = memory[param_one]
                    pass
                else:
                    print("[WARN] parameter mode != 0 for INPUT...")
                #print("[DEBUG] INPUT", inputs[0], "to", param_one)
                self.memory[param_one] = self.inqueue.get()
                instruction_pointer += 2
            elif opcode == 4:
                # OUTPUT
                param_one = self.memory[instruction_pointer+1]
                if parameter_mode_one == 0:
                    param_one = self.memory[param_one]
                #print("[DEBUG] OUTPUT", param_one)
                self.outqueue.put(param_one)
                output = param_one
                instruction_pointer += 2
            elif opcode == 5:
                # JUMP-IF-TRUE
                param_one = self.memory[instruction_pointer+1]
                if parameter_mode_one == 0:
                    param_one = self.memory[param_one]
                param_two = self.memory[instruction_pointer+2]
                if parameter_mode_two == 0:
                    param_two = self.memory[param_two]
                #print("[DEBUG] Jump-If-True", param_one, param_two)
                if param_one != 0:
                    instruction_pointer = param_two
                else:
                    instruction_pointer += 3
            elif opcode == 6:
                # JUMP-IF-FALSE
                param_one = self.memory[instruction_pointer+1]
                if parameter_mode_one == 0:
                    param_one = self.memory[param_one]
                param_two = self.memory[instruction_pointer+2]
                if parameter_mode_two == 0:
                    param_two = self.memory[param_two]
                #print("[DEBUG] Jump-If-False", param_one, param_two)
                if param_one == 0:
                    instruction_pointer = param_two
                else:
                    instruction_pointer += 3
            elif opcode == 7:
                # LESS THAN
                param_one = self.memory[instruction_pointer+1]
                if parameter_mode_one == 0:
                    param_one = self.memory[param_one]
                param_two = self.memory[instruction_pointer+2]
                if parameter_mode_two == 0:
                    param_two = self.memory[param_two]
                param_three = self.memory[instruction_pointer+3]
                if parameter_mode_three == 0:
                    #param_three = memory[param_three]
                    pass
                else:
                    print("[WARN] parameter mode != 0 for MUL...")
                #print("[DEBUG] LESS_THAN", param_one, param_two, param_three)
                if param_one < param_two:
                    self.memory[param_three] = 1
                else:
                    self.memory[param_three] = 0
                instruction_pointer += 4
            elif opcode == 8:
                # EQUALS
                param_one = self.memory[instruction_pointer+1]
                if parameter_mode_one == 0:
                    param_one = self.memory[param_one]
                param_two = self.memory[instruction_pointer+2]
                if parameter_mode_two == 0:
                    param_two = self.memory[param_two]
                param_three = self.memory[instruction_pointer+3]
                if parameter_mode_three == 0:
                    #param_three = self.memory[param_three]
                    pass
                else:
                    print("[WARN] parameter mode != 0 for MUL...")
                #print("[DEBUG] EQUALS", param_one, param_two, param_three)
                if param_one == param_two:
                    self.memory[param_three] = 1
                else:
                    self.memory[param_three] = 0
                instruction_pointer += 4
            elif opcode == 99:
                # halt
                running = False
            else:
                # something went wrong
                print("[ERROR] unknown Opcode:", opcode)
                running = False
        return output
