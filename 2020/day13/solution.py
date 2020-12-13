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


def format_n_a(times):
    n = []
    a = []

    for i, bus in enumerate(times.split(",")):
        if bus == "x":
            continue
        bus = int(bus)
        n.append(bus)
        a.append(bus - i)

    return (n, a)


# fmt: off
# I stole this code from HERE =>
# https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a * b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod
# <= to HERE

"""
    Chinese Remainder Theorem solves the following set of equations:
        x ≡ a0 mod n0
        x ≡ a1 mod n1
            ...
        x ≡ ai mod ni


    In this problem, we have:
        x + 0 ≡ a0 mod n0
        x + 1 ≡ a1 mod n1
            ...
        x + i ≡ ai mod ni

    Which rearranges to:
        x ≡ (a0 - 0) mod n0
        x ≡ (a1 - 1) mod n0
            ...
        x ≡ (ai - i) mod n0

    Therefore WLOG using bus times "17,x,13,19" and ignoring all times "x"
    N = [n0, n1, ..., ni]
      = [17, 13, 19]

    A = [(a0 - 0), (a1 - 1), ..., (ai - i)]
      = [(17 - 0), (13 - 2), (19 - 3)]
      = [17, 11, 16]
"""
# fmt: on

print(chinese_remainder(*format_n_a("17,x,13,19")))  # 3417
print(chinese_remainder([17, 13, 19], [17, 11, 16]))  # 3417
print(chinese_remainder(*format_n_a("67,7,59,61")))  # 754018
print(chinese_remainder(*format_n_a("1789,37,47,1889")))  # 1202161486
print(chinese_remainder(*format_n_a(times)))  # 775230782877242
