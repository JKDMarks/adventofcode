import re
import itertools
from copy import deepcopy
from pdb import set_trace as db


input_str = """#.#.#.##
.####..#
#####.#.
#####..#
#....###
###...##
...#.#.#
#.##..##"""
input = [list(s) for s in input_str.split("\n")]

dirs = [[-1, 0, 1]] * 3
neighbors = list(itertools.product(*dirs))
neighbors.remove((0, 0, 0))
# [(-1, -1, -1), (-1, -1, 0), (-1, -1, 1), ..., (1, 1, 1)]

test_str = """.#.
..#
###"""
test_input = [list(s) for s in test_str.split("\n")]


def create_inactive(input):
    h = len(input)
    w = len(input[0])
    return ([["."] * w]) * h


def check_pos(input, pos):
    z,y,x = pos
    if z not in input:
        input[z] = create_inactive(input[0])

    h,w = len(input[z]), len(input[z][0])
    if 0 <= y < h and 0 <= x < w:
        return input[z][y][x]


def check_neighbors(input, z,y,x):
    nbr_dict = {".": 0, "#": 0}

    for nbr in neighbors:
        pos = [(a+b) for (a,b) in zip(nbr, (z,y,x))]
        at_pos = check_pos(input, pos)
        if at_pos:
            nbr_dict[at_pos] += 1

    return nbr_dict


def count_active(input, cycles):
    input = {-1: create_inactive(input), 0: input, 1: create_inactive(input)}

    while cycles > 0:
        for k in input:
            next = deepcopy(input[k])
            for j in range(len(input[k])):
                for i in range(len(input[k][j])):
                    nbrs = check_neighbors(input, k,j,i)
                    if input[k][j][i] == '#':
                        next[j][i] = ('#' if (2 <= nbrs['#'] <= 3) else '.')
                    if input[k][j][i] == '.':
                        next[j][i] = ('#' if nbrs['#'] == 3 else '.')
                        
            # Left off here
            db()
        cycles -= 1

    return


print(count_active(test_input, 6))  # 112
# print(count_active(inpt, 6))
