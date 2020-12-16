import re
from functools import reduce
from pdb import set_trace as db


with open("raw-input.txt") as f:
    input = f.read().split("\n\n")


test_str = """class: 1-3 or 5-7
row: 6-11 or 33-44
seat: 13-40 or 45-50

your ticket:
7,1,14

nearby tickets:
7,3,47
40,4,50
55,2,20
38,6,12"""
test_input = test_str.split("\n\n")


def create_valid_ranges(ranges):
    range_dict = {}

    for range in ranges.split("\n"):
        name, values = range.split(": ")
        a, b, c, d = [int(n) for n in re.split("-| or ", values)]
        range_dict[name] = [a, b, c, d]

    return range_dict


def check_is_valid(range_arr, x):
    a, b, c, d = range_arr
    return (a <= x <= b) or (c <= x <= d)


def find_error_rate(input):
    [ranges, my_ticket, nearby_tix] = input
    ranges = create_valid_ranges(ranges)
    invalid_values = []

    for n in re.split(",|\n", nearby_tix[16:]):
        is_valid = False
        n = int(n)
        for range_arr in ranges.values():
            if check_is_valid(range_arr, n):
                is_valid = True
                break

        if not is_valid:
            invalid_values.append(n)

    return sum(invalid_values)


# print(find_error_rate(test_input))  # 71
# print(find_error_rate(input)) # 32842

test_str_2 = """class: 0-1 or 4-19
row: 0-5 or 8-19
seat: 0-13 or 16-19

your ticket:
11,12,13

nearby tickets:
3,9,18
15,1,5
5,14,9"""
test_input_2 = test_str_2.split("\n\n")


def check_ticket_valid(ticket, ranges):
    for n in ticket:
        valid_arr = [check_is_valid(range_arr, n) for range_arr in ranges.values()]
        if not any(valid_arr):
            return False

    return True


def check_range_valid(range_arr, nums):
    return all([check_is_valid(range_arr, n) for n in nums])


def find_positions(input):
    [ranges, my_ticket, nearby_tix] = input

    ranges = create_valid_ranges(ranges)
    tickets = [[int(n) for n in s.split(",")] for s in nearby_tix[16:].split("\n")]
    pos_dict = {i: [] for i in range(len(ranges))}

    for ticket in tickets:
        if check_ticket_valid(ticket, ranges):
            for (i, v) in enumerate(ticket):
                pos_dict[i].append(v)

    name_can_be = {}
    for (name, range_arr) in ranges.items():
        name_can_be[name] = [
            check_range_valid(range_arr, values) for (i, values) in pos_dict.items()
        ]

    l = len(name_can_be.keys())
    name_to_i = {}
    while len(name_to_i.keys()) < l:
        for (name, can_be) in name_can_be.items():
            if can_be.count(True) == 1:
                i = can_be.index(True)
                name_to_i[name] = i
                for k in name_can_be.keys():
                    name_can_be[k][i] = False

    my_ticket = [int(n) for n in my_ticket[13:].split(",")]
    departures_only = {
        k: v for (k, v) in name_to_i.items() if k.startswith("departure")
    }
    my_departures = [my_ticket[i] for i in departures_only.values()]

    return reduce(lambda a, b: a * b, my_departures)


# print(find_positions(test_input_2))
print(find_positions(input))  # 2628667251989
