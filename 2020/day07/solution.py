import json
from pdb import set_trace as db

with open("input.json") as f:
    input = json.load(f)

tgt = "shiny gold"

can_be_contained_by = {}
for [color, contains] in input.items():
    for contained_arr in contains:
        contained_color = contained_arr[1]
        if contained_color in can_be_contained_by:
            can_be_contained_by[contained_color].append(color)
        else:
            can_be_contained_by[contained_color] = [color]


COUNT = 0
SEEN = {}


def count_possiblities(tgt):
    if tgt in can_be_contained_by:
        for color in can_be_contained_by[tgt]:
            if color not in SEEN:
                SEEN[color] = True
                # COUNT += 1
                print(color)
                count_possiblities(color)


count_possiblities(tgt)
print(COUNT)
print(len(SEEN.keys()))
