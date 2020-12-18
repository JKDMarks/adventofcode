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


def expand_by_one(pos_dict):
    expanded = pos_dict.copy()

    for pos in pos_dict:
        x, y, z = [int(n) for n in pos.split(",")]
        for nbr in neighbors:
            check_pos = ",".join([str(a + b) for (a, b) in zip(nbr, (x, y, z))])
            if check_pos not in expanded:
                expanded[check_pos] = "."

    return expanded


def check_neighbors(pos_dict, pos):
    nbr_dict = {".": 0, "#": 0}
    x, y, z = [int(n) for n in pos.split(",")]
    for nbr in neighbors:
        check_pos = ",".join([str(a + b) for (a, b) in zip(nbr, (x, y, z))])
        if check_pos not in pos_dict:
            nbr_dict["."] += 1
        else:
            nbr_dict[pos_dict[check_pos]] += 1

        if nbr_dict["#"] > 3:
            break

    return nbr_dict


def run_one_cycle(pos_dict):
    pos_dict = expand_by_one(pos_dict)
    next = pos_dict.copy()

    for (pos, val) in pos_dict.items():
        nbrs = check_neighbors(pos_dict, pos)
        if val == "#":
            if 2 <= nbrs["#"] <= 3:
                next[pos] = "#"
            else:
                next[pos] = "."
        elif val == ".":
            if nbrs["#"] == 3:
                next[pos] = "#"
            else:
                next[pos] = "."

    return next


def count_active(input, cycles):
    pos_dict = {}
    for j in range(len(input)):
        for i in range(len(input[j])):
            pos = ",".join((str(i), str(j), "0"))
            pos_dict[pos] = input[j][i]

    while cycles > 0:
        pos_dict = run_one_cycle(pos_dict)
        cycles -= 1

    return list(pos_dict.values()).count("#")


# print(count_active(test_input, 6))  # 112
# print(count_active(input, 6))


dirs_4d = [[-1, 0, 1]] * 4
neighbors_4d = list(itertools.product(*dirs_4d))
neighbors_4d.remove((0, 0, 0, 0))


def expand_by_one_4d(pos_dict):
    expanded = pos_dict.copy()

    for pos in pos_dict:
        x, y, z, w = [int(n) for n in pos.split(",")]
        for nbr in neighbors_4d:
            check_pos = ",".join([str(a + b) for (a, b) in zip(nbr, (x, y, z, w))])
            if check_pos not in expanded:
                expanded[check_pos] = "."

    return expanded


def check_neighbors_4d(pos_dict, pos):
    nbr_dict = {".": 0, "#": 0}
    x, y, z, w = [int(n) for n in pos.split(",")]
    for nbr in neighbors_4d:
        check_pos = ",".join([str(a + b) for (a, b) in zip(nbr, (x, y, z, w))])
        if check_pos not in pos_dict:
            nbr_dict["."] += 1
        else:
            nbr_dict[pos_dict[check_pos]] += 1

        if nbr_dict["#"] > 3:
            break

    return nbr_dict


def run_one_cycle_4d(pos_dict):
    pos_dict = expand_by_one_4d(pos_dict)
    next = pos_dict.copy()

    for (pos, val) in pos_dict.items():
        nbrs = check_neighbors_4d(pos_dict, pos)
        if val == "#":
            if 2 <= nbrs["#"] <= 3:
                next[pos] = "#"
            else:
                next[pos] = "."
        elif val == ".":
            if nbrs["#"] == 3:
                next[pos] = "#"
            else:
                next[pos] = "."

    return next


def count_active_4d(input, cycles):
    pos_dict = {}
    for j in range(len(input)):
        for i in range(len(input[j])):
            pos = ",".join((str(i), str(j), "0", "0"))
            pos_dict[pos] = input[j][i]

    while cycles > 0:
        pos_dict = run_one_cycle_4d(pos_dict)
        cycles -= 1

    return list(pos_dict.values()).count("#")


# print(count_active_4d(test_input, 6))  # 848
# print(count_active_4d(input, 6))  # 1812
