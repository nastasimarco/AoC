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

--- Part Two ---
It turns out that this circuit is very timing-sensitive; you actually need to minimize the signal delay.

To do this, calculate the number of steps each wire takes to reach each intersection; choose the intersection where the sum of both wires' steps is lowest. If a wire visits a position on the grid multiple times, use the steps value from the first time it visits that position when calculating the total value of a specific intersection.

The number of steps a wire takes is the total number of grid squares the wire has entered to get to that location, including the intersection being considered. Again consider the example from above:

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
In the above example, the intersection closest to the central port is reached after 8+5+5+2 = 20 steps by the first wire and 7+6+4+3 = 20 steps by the second wire for a total of 20+20 = 40 steps.

However, the top-right intersection is better: the first wire takes only 8+5+2 = 15 and the second wire takes only 7+6+2 = 15, a total of 15+15 = 30 steps.

Here are the best steps for the extra examples from above:

R75,D30,R83,U83,L12,D49,R71,U7,L72
U62,R66,U55,R34,D71,R55,D58,R83 = 610 steps
R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51
U98,R91,D20,R16,D67,R40,U7,R15,U6,R7 = 410 steps
What is the fewest combined steps the wires must take to reach an intersection?
"""
import numpy as np
import matplotlib.pyplot as plt

with open('input.txt') as input_file:
    data = input_file.read()

# custom input
# data = 'R8,U5,L5,D3\nU7,R6,D4,L4\n'
# data = 'R75,D30,R83,U83,L12,D49,R71,U7,L72\n\
# U62,R66,U55,R34,D71,R55,D58,R83\n'

path_1, path_2 = data.split('\n')[0:2]
path_1 = path_1.split(',')
path_2 = path_2.split(',')

def path_calc(path_list):
    x_pos = np.zeros((len(path_list) + 1,), dtype=int)
    y_pos = np.zeros((len(path_list) + 1,), dtype=int)
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
    return np.array([x_pos, y_pos])

def vertical(segment):
    # segment must be a (2,2) shape np.array.
    if segment[1, 0] == segment[1, 1]:
        return False
    elif segment[0, 0] == segment[0, 1]:
        return True
    else:
        print('Something is wrong. Segment appears oblique.')

def segment_cross(segment1, segment2):
    if (vertical(segment1)):
        if (vertical(segment2)):
            # print('Two vertical segments...')
            return None, None
            # pass
        else:
            if (min(segment2[0,:]) <= segment1[0,0] <= max(segment2[0,:]))\
                and\
                (min(segment1[1,:]) <= segment2[1,0] <= max(segment1[1,:])):
            # if (list(segment1[0, 0] >= segment2[0, :]).count(True) == 1)\
            #    and\
            #    (list(segment2[1, 0] >= segment1[1, :]).count(True) == 1):
                # return True
                return segment1[0,0], segment2[1,0]
            else:
                # return False
                return None, None
    else:
        if (vertical(segment2)):
            if (min(segment1[0,:]) <= segment2[0,0] <= max(segment1[0,:]))\
                and\
                (min(segment2[1,:]) <= segment1[1,0] <= max(segment2[1,:])):
            # if (list(segment1[1, 0] >= segment2[1, :]).count(True) == 1)\
            #    and\
            #    (list(segment2[0, 0] >= segment1[0, :]).count(True) == 1):
                # return True
                return segment2[0,0], segment1[1,0]
            else:
                # return False
                return None, None
        else:
            return None, None
        #     print('Two horizontal segments...')

# segment_1 = pos_1[:, :2]
# segment_2 = pos_2[:, :2]

def cross_array(pos1, pos2):
    cross_x = []
    cross_y = []
    for i in range(len(pos1[0]) - 1):
        for j in range(len(pos2[0]) - 1):
            cross = segment_cross(pos1[:, i:i+2], pos2[:, j:j+2])
            if (cross == (None, None)):
                pass
            else:
                cross_x += [cross[0]]
                cross_y += [cross[1]]
    return np.array([cross_x, cross_y])

pos_1 = path_calc(path_1)
pos_2 = path_calc(path_2)

cross = cross_array(pos_1, pos_2)
cross_distances = np.sum(np.abs(cross), 0)
closest_cross = min(cross_distances[cross_distances > 0])

print('Part I')
print(f'The Manhattan distance from the central port to the closest\
intersection is: {closest_cross}')

plt.plot(pos_1[0], pos_1[1], '.-', pos_2[0], pos_2[1], '.-')
plt.plot(cross[0], cross[1], 'o')