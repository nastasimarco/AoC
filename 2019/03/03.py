"""Solution attempt of AoC 2019 puzzle 03.

--- Day 3: Crossed Wires ---
The gravity assist was successful, and you're well on your way to the Venus refuelling station. During the rush back on Earth, the fuel management system wasn't completely installed, so that's next on the priority list.

Opening the front panel reveals a jumble of wires. Specifically, two wires are connected to a central port and extend outward on a grid. You trace the path each wire takes as it leaves the central port, one wire per line of text (your puzzle input).

The wires twist and turn, but the two wires occasionally cross paths. To fix the circuit, you need to find the intersection point closest to the central port. Because the wires are on a grid, use the Manhattan distance for this measurement. While the wires do technically cross right at the central port where they both start, this point does not count, nor does a wire count as crossing with itself.

For example, if the first wire's path is R8,U5,L5,D3, then starting from the central port (o), it goes right 8, up 5, left 5, and finally down 3:

...........
...........
...........
....+----+.
....|....|.
....|....|.
....|....|.
.........|.
.o-------+.
...........
Then, if the second wire's path is U7,R6,D4,L4, it goes up 7, right 6, down 4, and left 4:

...........
.+-----+...
.|.....|...
.|..+--X-+.
.|..|..|.|.
.|.-X--+.|.
.|..|....|.
.|.......|.
.o-------+.
...........
These wires cross at two locations (marked X), but the lower-left one is closer to the central port: its distance is 3 + 3 = 6.

Here are a few more examples:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = distance 159
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = distance 135
What is the Manhattan distance from the central port to the closest intersection?
"""
import numpy as np
import matplotlib.pyplot as plt

with open('input.txt') as input_file:
    data = input_file.read()

# custom input
# data = 'R8,U5,L5,D3\nU7,R6,D4,L4\n'

path_1, path_2 = data.split('\n')[0:2]
path_1 = path_1.split(',')
path_2 = path_2.split(',')

# def path_calc(path_list):
#     x_pos = [0]
#     y_pos = [0]
#     # print(x_pos, y_pos, '\n')
#     for i in range(len(path_list)):
#         if path_list[i].startswith('R'):
#             x_pos += [x_pos[-1] + int(path_list[i][1:])]
#             y_pos += [y_pos[-1]]
#         elif path_list[i].startswith('L'):
#             x_pos += [x_pos[-1] - int(path_list[i][1:])]
#             y_pos += [y_pos[-1]]
#         elif path_list[i].startswith('U'):
#             x_pos += [x_pos[-1]]
#             y_pos += [y_pos[-1] + int(path_list[i][1:])]
#         elif path_list[i].startswith('D'):
#             x_pos += [x_pos[-1]]
#             y_pos += [y_pos[-1] - int(path_list[i][1:])]
#         else: print("C'è qualquadra che non cosa!")
#         # print(x_pos, y_pos, '\n')
#     return x_pos, y_pos

def path_calc(path_list):
    x_pos = np.zeros((len(path_list)+1,), dtype=int)
    y_pos = np.zeros((len(path_list)+1,), dtype=int)
    # print(x_pos, y_pos, '\n')
    for i in range(len(path_list)):
        if path_list[i].startswith('R'):
            x_pos[i+1] = x_pos[i] + int(path_list[i][1:])
            y_pos[i+1] = y_pos[i]
        elif path_list[i].startswith('L'):
            x_pos[i+1] = x_pos[i] - int(path_list[i][1:])
            y_pos[i+1] = y_pos[i]
        elif path_list[i].startswith('U'):
            x_pos[i+1] = x_pos[i]
            y_pos[i+1] = y_pos[i] + int(path_list[i][1:])
        elif path_list[i].startswith('D'):
            x_pos[i+1] = x_pos[i]
            y_pos[i+1] = y_pos[i] - int(path_list[i][1:])
        else: print("C'è qualquadra che non cosa!")
        # print(x_pos, y_pos, '\n')
    return x_pos, y_pos

def segment(pos_array):
    # pos_array[]
    pass

# def segment_cross(pos_list_1, pos_list_2):
#     for i in range(0, len(pos_list_1[0]), 2):
#         for j in range0, len(0, pos_list_2[0]), 2):
#             if 
#     return cross_list

pos_1 = path_calc(path_1)
pos_2 = path_calc(path_2)

plt.plot(pos_1[0], pos_1[1], '.-', pos_2[0], pos_2[1], '.-')