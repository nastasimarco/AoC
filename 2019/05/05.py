"""Solution attempt of AoC 2019 puzzle 05.

--- Day 5: Sunny with a Chance of Asteroids ---
You're starting to sweat as the ship makes its way toward Mercury. The Elves suggest that you get the air conditioner working by upgrading your ship computer to support the Thermal Environment Supervision Terminal.

The Thermal Environment Supervision Terminal (TEST) starts by running a diagnostic program (your puzzle input). The TEST diagnostic program will run on your existing Intcode computer after a few modifications:

First, you'll need to add two new instructions:

Opcode 3 takes a single integer as input and saves it to the position given by its only parameter. For example, the instruction 3,50 would take an input value and store it at address 50.
Opcode 4 outputs the value of its only parameter. For example, the instruction 4,50 would output the value at address 50.
Programs that use these instructions will come with documentation that explains what should be connected to the input and output. The program 3,0,4,0,99 outputs whatever it gets as input, then halts.

Second, you'll need to add support for parameter modes:

Each parameter of an instruction is handled based on its parameter mode. Right now, your ship computer already understands parameter mode 0, position mode, which causes the parameter to be interpreted as a position - if the parameter is 50, its value is the value stored at address 50 in memory. Until now, all parameters have been in position mode.

Now, your ship computer will also need to handle parameters in mode 1, immediate mode. In immediate mode, a parameter is interpreted as a value - if the parameter is 50, its value is simply 50.

Parameter modes are stored in the same value as the instruction's opcode. The opcode is a two-digit number based only on the ones and tens digit of the value, that is, the opcode is the rightmost two digits of the first value in an instruction. Parameter modes are single digits, one per parameter, read right-to-left from the opcode: the first parameter's mode is in the hundreds digit, the second parameter's mode is in the thousands digit, the third parameter's mode is in the ten-thousands digit, and so on. Any missing modes are 0.

For example, consider the program 1002,4,3,4,33.

The first instruction, 1002,4,3,4, is a multiply instruction - the rightmost two digits of the first value, 02, indicate opcode 2, multiplication. Then, going right to left, the parameter modes are 0 (hundreds digit), 1 (thousands digit), and 0 (ten-thousands digit, not present and therefore zero):

ABCDE
 1002

DE - two-digit opcode,      02 == opcode 2
 C - mode of 1st parameter,  0 == position mode
 B - mode of 2nd parameter,  1 == immediate mode
 A - mode of 3rd parameter,  0 == position mode,
                                  omitted due to being a leading zero
This instruction multiplies its first two parameters. The first parameter, 4 in position mode, works like it did before - its value is the value stored at address 4 (33). The second parameter, 3 in immediate mode, simply has value 3. The result of this operation, 33 * 3 = 99, is written according to the third parameter, 4 in position mode, which also works like it did before - 99 is written to address 4.

Parameters that an instruction writes to will never be in immediate mode.

Finally, some notes:

It is important to remember that the instruction pointer should increase by the number of values in the instruction after the instruction finishes. Because of the new instructions, this amount is no longer always 4.
Integers can be negative: 1101,100,-1,4,0 is a valid program (find 100 + -1, store the result in position 4).
The TEST diagnostic program will start by requesting from the user the ID of the system to test by running an input instruction - provide it 1, the ID for the ship's air conditioner unit.

It will then perform a series of diagnostic tests confirming that various parts of the Intcode computer, like parameter modes, function correctly. For each test, it will run an output instruction indicating how far the result of the test was from the expected value, where 0 means the test was successful. Non-zero outputs mean that a function is not working correctly; check the instructions that were run before the output instruction to see which one failed.

Finally, the program will output a diagnostic code and immediately halt. This final output isn't an error; an output followed immediately by a halt means the program finished. If all outputs were zero except the diagnostic code, the diagnostic program ran successfully.

After providing 1 to the only input instruction and passing all the tests, what diagnostic code does the program produce?
"""

import numpy as np

input_instruction = 1
filename = 'input.txt'

with open(filename, 'r') as file:
    code = file.read()

code_array = np.loadtxt(filename, delimiter=',', dtype='int')

# custom input
# code = '3,0,4,0,99'
# code = '1002,4,3,4,33'
# code_list = code.split(',')
# code_array = np.array(code_list, dtype='int')
# code_array = np.array(code.split(','), dtype='int')
# print('Initial code:', code_array)
# print('Input:', input_instruction)

def code_compute(code, input_instruction):
    i = 0
    diagnostic_code = None
    while i < len(code):
        parameter_1 = None
        parameter_2 = None
        parameter_3 = None
        # halt program opcode
        if code[i]%100 == 99:
            return diagnostic_code
        # addition opcode, 3 parameters
        elif code[i]%100 == 1:
            # parameter 1 mode selection
            if (code[i]//100)%10 == 1: # immediate mode
                    parameter_1 = code[i+1]
            elif(code[i]//100)%10 == 0: # position mode
                    parameter_1 = code[code[i+1]]
            else:
                print('\nmacheccazz...\n')
            # parameter 2 mode selection
            if (code[i]//1000)%10 == 1: # immediate mode
                parameter_2 = code[i+2]
            elif(code[i]//1000)%10 == 0: # position mode
                parameter_2 = code[code[i+2]]
            else:
                print('\nmacheccazz...\n')
            # parameter 3 is always in position mode
            parameter_3 = code[i+3]
            # opcode execution
            code[parameter_3] = parameter_1 + parameter_2
            i += 4
            print(f'{parameter_1} + {parameter_2} at position {parameter_3}')
        # multiplication opcode, 3 parameters
        elif code[i]%100 == 2:
            # parameter 1 mode selection
            if (code[i]//100)%10 == 1: # immediate mode
                    parameter_1 = code[i+1]
            elif(code[i]//100)%10 == 0: # position mode
                    parameter_1 = code[code[i+1]]
            else:
                print('\nmacheccazz...\n')
            # parameter 2 mode selection
            if (code[i]//1000)%10 == 1: # immediate mode
                parameter_2 = code[i+2]
            elif(code[i]//1000)%10 == 0: # position mode
                parameter_2 = code[code[i+2]]
            else:
                print('\nmacheccazz...\n')
            # parameter 3 is always in position mode
            parameter_3 = code[i+3]
            # opcode execution
            code[parameter_3] = parameter_1 * parameter_2
            i += 4
            print(f'{parameter_1} * {parameter_2} at position {parameter_3}')
        # input opcode, 1 parameter
        elif code[i]%100 == 3:
            # parameter 1 mode selection
            if (code[i]//100)%10 == 1: # immediate mode
                    parameter_1 = code[i+1]
            elif(code[i]//100)%10 == 0: # position mode
                    parameter_1 = code[i+1]
            else:
                print('\nmacheccazz...\n')
            # opcode execution
            code[parameter_1] = input_instruction
            i += 2
            print(f'input {input_instruction} at position {parameter_1}')
        # output opcode, 1 parameter
        elif code[i]%100 == 4:
            # parameter 1 mode selection
            if (code[i]//100)%10 == 1: # immediate mode
                    parameter_1 = code[i+1]
            elif(code[i]//100)%10 == 0: # position mode
                    parameter_1 = code[i+1]
            else:
                print('\nmacheccazz...\n')
            # opcode execution
            diagnostic_code = code[parameter_1]
            i += 2
            print(f'value at position {parameter_1} to output:',
                  f'Test produces {diagnostic_code}')
        else:
            print('\nmacheccazz...\n')

diagnostic_code = code_compute(code_array, input_instruction)
print('Final diagnostic code is:', diagnostic_code)
# print('Final code:', code_array)