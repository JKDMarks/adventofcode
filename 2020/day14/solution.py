import re
from pdb import set_trace as db

with open("raw-input.txt") as f:
    input = f.read().split("\n")

test_str = """mask = XXXXXXXXXXXXXXXXXXXXXXXXXXXXX1XXXX0X
mem[8] = 11
mem[7] = 101
mem[8] = 0"""
test_input = test_str.split("\n")


def split_instr(instr):
    return instr.split(" = ")


def pad_value(value):
    return format(value, "b").zfill(36)


def find_mem_addr(mem_str):
    return int(re.search("\[(\d+)\]", mem_str).group(1))


def apply_mask(value, mask):
    mask_applied = [(m if m != "X" else v) for (v, m) in zip(list(value), list(mask))]
    return int("".join(mask_applied), 2)


def run_program(program):
    mask = "X" * 36
    mem = {}

    for instr in program:
        cmd, val = split_instr(instr)
        if cmd == "mask":
            mask = val
        else:  # cmd == mem[#]
            mem_addr = find_mem_addr(cmd)
            res = apply_mask(pad_value(val), mask)
            mem[mem_addr] = res

    return sum(mem.values())


# print(run_program(test_input)) # 165
# print(run_program(input)) # 14925946402938

test_str_2 = """mask = 000000000000000000000000000000X1001X
mem[42] = 100
mask = 00000000000000000000000000000000X0XX
mem[26] = 1"""
test_input_2 = test_str_2.split("\n")


def find_addrs(addr, mask):
    mask_applied = [(a if m == "0" else m) for (a, m) in zip(list(addr), list(mask))]
    addr = "".join(mask_applied)
    exes = [i for (i, c) in enumerate(addr) if c == "X"]

    max_bin = 2 ** len(exes) - 1
    longest = len(format(max_bin - 1, "b"))
    bin_options = [format(i, "b").zfill(longest) for i in range(2 ** len(exes))]

    addrs = []
    for opt in bin_options:
        digits = [int(i) for i in list(opt)]
        mask = "".join(
            [
                (str(digits[exes.index(i)]) if i in exes else n)
                for (i, n) in enumerate(addr)
            ]
        )
        res = apply_mask(addr, mask)
        addrs.append(res)

    return addrs


def run_program_v2(program):
    mask = "X" * 36
    mem = {}

    for instr in program:
        cmd, val = split_instr(instr)
        if cmd == "mask":
            mask = val
        else:
            addr = pad_value((find_mem_addr(cmd)))
            addrs = find_addrs(addr, mask)
            for addr in addrs:
                mem[addr] = int(val)

    return sum(mem.values())


# print(run_program_v2(test_input_2))  # 208
# print(run_program_v2(input))  # 3706820676200
