import re
from pdb import set_trace as db

input = [int(n) for n in "15,5,1,4,7,0".split(",")]
test_input_1 = [int(n) for n in "0,3,6".split(",")]
test_input_2 = [int(n) for n in "1,3,2".split(",")]
test_input_3 = [int(n) for n in "3,1,2".split(",")]


def nth_num_said(input, tgt_num):
    turn = 0
    prev = None
    last_seen = {}

    for n in input:
        turn += 1
        last_seen[n] = [turn]
        prev = n

    def add_if_exists(prev, turn):
        if prev in last_seen:
            last_seen[prev].insert(0, turn)
            del last_seen[prev][2:]
        else:
            last_seen[prev] = [turn]

    while turn < tgt_num:
        turn += 1
        if turn % 100000 == 0:
            print(turn)

        if len(last_seen[prev]) == 1:
            prev = 0
            add_if_exists(prev, turn)
        else:
            prev = last_seen[prev][0] - last_seen[prev][1]
            add_if_exists(prev, turn)

    return prev


print(nth_num_said(test_input_1, 2020))  # 436
print(nth_num_said(test_input_2, 2020))  # 1
print(nth_num_said(test_input_3, 2020))  # 1259
print(nth_num_said(input, 2020))  # 1259

# print(nth_num_said(test_input_1, 30000000)) # 175594
print(nth_num_said(input, 30000000)) # 175594

