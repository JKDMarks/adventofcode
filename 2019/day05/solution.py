import json
from pdb import set_trace as db
from pprint import pprint as pp

with open("input.json") as f:
    arr = json.load(f)

global output
output = [0]


def run_program(input):
    def parse_opcode(unpadded_opcode, a, b, c, start_i):
        opcode = ("0" * (5 - len(unpadded_opcode))) + unpadded_opcode
        mode3, mode2, mode1, operation = opcode[0], opcode[1], opcode[2], opcode[3:5]
        num_params = 0
        if operation == "01":
            num_params = 3
            arr[c if mode3 == "0" else i + 3] = (arr[a] if mode1 == "0" else a) + (
                arr[b] if mode2 == "0" else b
            )
        elif operation == "02":
            num_params = 3
            arr[c if mode3 == "0" else i + 3] = (arr[a] if mode1 == "0" else a) * (
                arr[b] if mode2 == "0" else b
            )
        elif operation == "03":
            num_params = 1
            arr[a if mode1 == "0" else i + 1] = input
        elif operation == "04":
            num_params = 1
            output[0] = arr[a if mode1 == "0" else i + 1]

        return num_params

    # def handle1(a, b, c):
    #     arr[c] = arr[a] + arr[b]

    # def handle2(a, b, c):
    #     arr[c] = arr[a] * arr[b]

    i = 0
    while i < len(arr):
        curr = str(arr[i])
        a, b, c = (
            [int(n) for n in arr[i + 1 : i + 4]]
            if i + 4 < len(arr)
            else [None, None, None]
        )

        if curr == 99:
            break
        else:
            # print(curr, a, b, c, i)
            num_params = parse_opcode(curr, a, b, c, i)
        i += 1 + num_params

    return output


print(run_program(1))

# target = 19690720

# for x in range(100):
#     for y in range(100):
#         output = run_program(x, y)
#         if output == target:
#             print(x, y, output)  # 67 18 19690720
