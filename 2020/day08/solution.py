import json
import re
from pdb import set_trace as db

with open("raw-input.txt") as f:
    txt = f.read()
    input = txt.split("\n")

test_input = """nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6""".split(
    "\n"
)


def run_instructions(input):
    already_run = {}
    acc = 0
    i = 0
    is_infinite = False
    while i < len(input):
        if i in already_run:
            is_infinite = True
            break

        op, arg = input[i].split(" ")
        arg = int(arg)
        already_run[i] = True
        if op == "acc":
            acc += arg
            i += 1
        elif op == "jmp":
            i += arg
        elif op == "nop":
            i += 1

    if not is_infinite:
        print(acc)
    return acc


print(run_instructions(input))  # 1867


def find_broken_instruction(input):
    for (i, instr) in enumerate(input):
        op, arg = instr.split(" ")
        arg = int(arg)
        input_copy = input[:]

        if op == "jmp":
            input_copy[i] = "nop" + input_copy[i][3:]
        elif op == "nop":
            input_copy[i] = "jmp" + input_copy[i][3:]
        elif op == "acc":
            continue

        run_instructions(input_copy)


find_broken_instruction(input)  # 1303
