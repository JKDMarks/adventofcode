import json
import math
from pdb import set_trace as db

with open("./input.json") as input:
    arr = json.loads(input.read())

# 944, 554
# console.log(getSeatId(findSeat('BFFFBBFRRR'))); // 70, 7, 567
# console.log(getSeatId(findSeat('FFFBBBFRRR'))); // 14, 7, 119
# console.log(getSeatId(findSeat('BBFFBBFRLL'))); // 102, 4, 820


def parse_letter(l):
    return "0" if l == "F" or l == "L" else "1"


def arr_to_int(arr):
    return int("".join(arr), 2)


def get_seat_id(seat_str):
    return arr_to_int([parse_letter(l) for l in seat_str])


seats_taken = {}


def get_highest_seat(seats):
    highest = -1
    for seat in seats:
        seat_id = get_seat_id(seat)
        seats_taken[seat_id] = True
        highest = max(highest, seat_id)

    return highest


print(get_highest_seat(arr))

for seat in seats_taken:
    if ((seat + 1) not in seats_taken) and ((seat + 2) in seats_taken):
        print(seat + 1)
