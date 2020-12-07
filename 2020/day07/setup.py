import json
from pdb import set_trace as db

with open("raw-input.txt") as f:
    txt = f.read()

input = txt.split("\n")


def parse_bag_str(str):
    str = str.split(" contain ")
    bag_color = str[0].split(" bags")[0]
    output = [bag_color, []]

    if str[1] != "no other bags.":
        contained_bags = str[1].split(", ")
        for bag in contained_bags:
            qty = int(bag[0])
            color_in_bag = bag.split(" bags")[0][2:]
            output[1].append([qty, color_in_bag])

    return output


bag_rules = {}
for rule in input:
    [k, v] = parse_bag_str(rule)
    bag_rules[k] = v

print(bag_rules)

with open("input.json", "r") as f:
    input = json.load(f)
    with open("input.json", "w") as f:
        json.dump(bag_rules, f)