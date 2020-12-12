from pdb import set_trace as db

with open("raw-input.txt") as f:
    dirs = f.read().split("\n")

test_str = """F10
N3
F7
R90
F11"""
test_dirs = test_str.split("\n")


cardinal_dict = {"N": [0, 1], "S": [0, -1], "E": [1, 0], "W": [-1, 0]}

turn_right = ["N", "E", "S", "W"]
turn_left = ["N", "W", "S", "E"]


def turn_ship(facing, direction, degree):
    turn_ct = degree // 90

    if direction == "R":
        return turn_right[(turn_right.index(facing) + turn_ct) % len(turn_right)]

    elif direction == "L":
        return turn_left[(turn_left.index(facing) + turn_ct) % len(turn_left)]


def move(pos, cardinality, spaces):
    base_move = cardinal_dict[cardinality]
    move_arr = [x * spaces for x in base_move]

    return [x + y for x, y in zip(pos, move_arr)]


def follow_dirs(dirs):
    facing = "E"
    pos = [0, 0]
    for dir in dirs:
        action, num = dir[0], int(dir[1:])

        if action in ["N", "S", "E", "W"]:
            pos = move(pos, action, num)

        elif action == "F":
            pos = move(pos, facing, num)

        elif action in ["L", "R"]:
            facing = turn_ship(facing, action, num)

    print(pos)
    return abs(pos[0]) + abs(pos[1])


# print(follow_dirs(test_dirs))  # [17, -8], 25
# print(follow_dirs(dirs))  # [1269, -1011], 2280


def rotate_wapyt(waypt_pos, direction, degree):
    turn_ct = degree // 90
    if direction == "L":
        direction = "R"
        turn_ct = 4 - turn_ct

    for i in range(turn_ct):
        waypt_pos = [waypt_pos[1], -1 * waypt_pos[0]]

    return waypt_pos


def true_follow_dirs(dirs):
    ship_pos = [0, 0]
    waypt_pos = [10, 1]

    for dir in dirs:
        action, num = dir[0], int(dir[1:])

        if action in ["N", "S", "E", "W"]:
            waypt_pos = move(waypt_pos, action, num)

        elif action == "F":
            move_arr = [x * num for x in waypt_pos]
            ship_pos = [x + y for (x, y) in zip(ship_pos, move_arr)]

        elif action in ["L", "R"]:
            waypt_pos = rotate_wapyt(waypt_pos, action, num)

    print(ship_pos)
    return abs(ship_pos[0]) + abs(ship_pos[1])


print(true_follow_dirs(test_dirs))  # [214, -72], 286
print(true_follow_dirs(dirs))  # [12863, -25830], 38693
