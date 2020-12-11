from pdb import set_trace as db
from copy import deepcopy

with open("raw-input.txt") as f:
    seats = [list(s) for s in f.read().split("\n")]

# fmt: off
test_str_1 = """L.LL.LL.LL
                LLLLLLL.LL
                L.L.L..L..
                LLLL.LL.LL
                L.LL.LL.LL
                L.LLLLL.LL
                ..L.L.....
                LLLLLLLLLL
                L.LLLLLL.L
                L.LLLLL.LL""".replace(' ', '')
# fmt: on
test_seats_1 = [list(s) for s in test_str_1.split("\n")]

# L: empty
# .: floor
# #: occupied


def adj_seats_1(seats, y, x, h, w):
    adj_dict = {"L": 0, "#": 0, ".": 0}
    adj_dict[seats[y][x]] -= 1

    for i in range(x - 1, x + 2):
        for j in range(y - 1, y + 2):
            if 0 <= j and j < h and 0 <= i and i < w:
                adj_dict[seats[j][i]] += 1

    return adj_dict


def sit_1(seats):
    copy = deepcopy(seats)
    width = len(seats[0])
    height = len(seats)
    for (j, row) in enumerate(seats):
        for (i, seat) in enumerate(row):
            adj_dict = adj_seats_1(seats, j, i, height, width)
            if seat == "L" and adj_dict["#"] == 0:
                copy[j][i] = "#"
            elif seat == "#" and adj_dict["#"] >= 4:
                copy[j][i] = "L"

    return copy


def count_occupied_1(seats):
    next = sit_1(seats)
    while seats != next:
        seats, next = next, sit_1(next)

    return [s for r in seats for s in r].count("#")


# print(count_occupied_1(test_seats_1))  # 37
# print(count_occupied_1(seats))  # 2346


directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


def in_arr(seats, y, x):
    h, w = len(seats), len(seats[0])
    return 0 <= y < h and 0 <= x < w


def adj_seats_2(seats, y, x):
    adj_dict = {"L": 0, "#": 0, ".": 0}

    for (dy, dx) in directions:
        j, i = y + dy, x + dx
        while in_arr(seats, j, i):
            if seats[j][i] in ["L", "#"]:
                adj_dict[seats[j][i]] += 1
                break
            else:
                j, i = j + dy, i + dx

    return adj_dict


def sit_2(seats):
    copy = deepcopy(seats)

    for (j, row) in enumerate(seats):
        for (i, seat) in enumerate(row):
            adj_dict = adj_seats_2(seats, j, i)
            if seat == "L" and adj_dict["#"] == 0:
                copy[j][i] = "#"
            elif seat == "#" and adj_dict["#"] >= 5:
                copy[j][i] = "L"

    return copy


def count_occupied_2(seats):
    next = sit_2(seats)
    while seats != next:
        seats, next = next, sit_2(next)

    return [s for r in seats for s in r].count("#")


# print(count_occupied_2(test_seats_1))  # 26
# print(count_occupied_2(seats))  # 2111
