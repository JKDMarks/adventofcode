import json
from pdb import set_trace as db
from pprint import pprint as pp

with open("../day02/input.json") as f:
    input = json.load(f)


def run_program(p1, p2):
    arr = [input[0], p1, p2] + input[3:]

    def handle1(a, b, c):
        arr[c] = arr[a] + arr[b]

    def handle2(a, b, c):
        arr[c] = arr[a] * arr[b]

    i = 0
    while i <= len(arr):
        [curr, a, b, c] = arr[i : i + 4]
        if curr == 1:
            handle1(a, b, c)
        elif curr == 2:
            handle2(a, b, c)
        elif curr == 99:
            break
        i += 4

    return arr[0]


print(run_program(12, 2))

target = 19690720

for x in range(100):
    for y in range(100):
        output = run_program(x, y)
        if output == target:
            print(x, y, output)  # 67 18 19690720
