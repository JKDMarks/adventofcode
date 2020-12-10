import re

from itertools import combinations
import operator as op
from functools import reduce
from pdb import set_trace as db

with open("raw-input.txt") as f:
    input = [0] + sorted([int(n) for n in f.read().split("\n")])
    input.append(input[-1] + 3)


test_str_1 = """16
10
15
5
1
11
7
19
6
12
4"""
test_input_1 = [0] + sorted([int(n) for n in test_str_1.split("\n")])
test_input_1.append(test_input_1[-1] + 3)
print(test_input_1)

test_str_2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
test_input_2 = [0] + sorted([int(n) for n in test_str_2.split("\n")])
test_input_2.append(test_input_2[-1] + 3)
print(test_input_2)


def count_jolt_diffs(input):
    diff_ct_dict = {1: 0, 2: 0, 3: 0}

    for (i, n) in enumerate(input):
        if i == 0:
            diff_ct_dict[n] += 1

        if i == len(input) - 1:
            diff_ct_dict[3] += 1
        else:
            next = input[i + 1]
            diff_ct_dict[next - n] += 1

    print(diff_ct_dict[1] * diff_ct_dict[3])
    return diff_ct_dict


# print(count_jolt_diffs(test_input_1))  # 35
# print(count_jolt_diffs(test_input_2))  # 220
# print(count_jolt_diffs(input))  # 2059

# def check_next_3(a,b):


def find_skippable(input):
    # skip1 = 0
    # skip2 = 0
    skippable = set()

    for (i, n) in enumerate(input):
        next1st = input[i + 1] if i + 1 < len(input) else None
        next2nd = input[i + 2] if i + 2 < len(input) else None

        if next2nd and next2nd <= n + 3:
            skippable.add(next1st)

    return skippable


def is_valid_skip(input, skip):
    copy = input[:]
    for n in skip:
        copy.remove(n)

    for (i, n) in enumerate(copy):
        if i == len(copy) - 1:
            continue
        else:
            next = copy[i + 1]
            if n + 3 < next:
                return False

    return True


def count_possible_combinations(input):
    skippable = find_skippable(input)
    count = 0

    for i in range(len(skippable) + 1):
        skip_tuples = list(combinations(skippable, i))
        print(skip_tuples)
        # print(skip_tuples)
        for skip in skip_tuples:
            if is_valid_skip(input, skip):
                count += 1

    return count


# print(count_possible_combinations(test_input_1))
# print(count_possible_combinations(test_input_2))
print(count_possible_combinations(input))
