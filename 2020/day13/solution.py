from pdb import set_trace as db
from math import gcd
from functools import reduce

with open("raw-input.txt") as f:
    input = f.read().split("\n")
    times = input[1]

test_str = """939
7,13,x,x,59,x,31,19"""
test_input = test_str.split("\n")


def soonest_bus(input):
    depart = int(input[0])
    busses = [int(x) for x in input[1].split(",") if x.isnumeric()]

    soonest = -1
    for bus_id in busses:
        wait_time = depart % bus_id
        if wait_time == 0:
            soonest = bus_id

        else:
            soonest = max(soonest, bus_id)

    return soonest


def find_solution_1(input):
    depart = int(input[0])
    bus_id = soonest_bus(input)
    wait_time = bus_id - (depart % bus_id)

    return bus_id * wait_time


# print(find_solution_1(test_input))  # 295
# print(find_solution_1(input))  # 8063


def lcm(a, b):
    return abs(a * b) // gcd(a, b)


def is_solution(times, unique_times, n):
    is_valid = True
    time = times[0] * n

    for (i, t) in unique_times:
        if (time + i) % t != 0:
            is_valid = False
            break

    return is_valid


def find_unique_times(times):
    return [(i, t) for (i, t) in enumerate(times) if t != 1]


# This *does* work but, again, supercomputer etc. etc.
def find_solution_2(times):
    times = [int(x) if x.isnumeric() else 1 for x in times.split(",")]
    unique_times = find_unique_times(times)

    n = 0
    is_valid = False

    while not is_valid:
        is_valid = is_solution(times, unique_times, n)
        n += 1

    return times[0] * (n - 1)


# print(find_solution_2("17,x,13,19"))  # 3417
# print(find_solution_2("67,7,59,61"))  # 754018
# print(find_solution_2("1789,37,47,1889"))  # 1202161486
# print(find_solution_2(times))  # 775230782877242
