import re
from pdb import set_trace as db

with open("raw-input.txt") as f:
    txt = f.read()
    input = txt.split("\n")


def parse_bag_str(str):
    str = str.split(" contain ")
    bag_color = str[0].split(" bags")[0]
    output = []

    if str[1] != "no other bags.":
        contained_bags = str[1].split(", ")
        for bag in contained_bags:
            qty = int(bag[0])
            color_in_bag = re.split(" bag(s)?", bag)[0][2:]
            output.append([qty, color_in_bag])

    return [bag_color, output]


bag_rules = {}
for rule in input:
    [k, v] = parse_bag_str(rule)
    bag_rules[k] = v


def count_possible_containers(rules, tgt):
    can_be_contained_by = {}
    for [containing_color, can_contain_arr] in rules.items():
        for [qty, contained_color] in can_contain_arr:
            if contained_color in can_be_contained_by:
                can_be_contained_by[contained_color].append(containing_color)
            else:
                can_be_contained_by[contained_color] = []
                can_be_contained_by[contained_color].append(containing_color)

    colors_seen = {}
    to_check = []

    for color in can_be_contained_by[tgt]:
        colors_seen[color] = True
        to_check.append(color)

    while len(to_check) > 0:
        check = to_check.pop(0)
        if check in can_be_contained_by:
            for color in can_be_contained_by[check]:
                if color not in colors_seen:
                    colors_seen[color] = True
                    to_check.append(color)

    return len(colors_seen.keys())


print(count_possible_containers(bag_rules, "shiny gold"))  # 164


def count_contained(rules, tgt, multiplier):
    count_arr = []

    def run(tgt, multiplier):
        can_contain_arr = rules[tgt]
        for [qty, contained_color] in can_contain_arr:
            count_arr.append(qty * multiplier)
            run(contained_color, qty * multiplier)

    run(tgt, multiplier)
    return sum(count_arr)


print(count_contained(bag_rules, "shiny gold", 1))  # 7872
