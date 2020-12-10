from pdb import set_trace as db


def sort_nums(nums):
    sorted_list = [0] + sorted([int(n) for n in nums.split("\n")])
    sorted_list.append(sorted_list[-1] + 3)
    return sorted_list


with open("raw-input.txt") as f:
    input = sort_nums(f.read())

test_str_1 = """16
10
15
5
1
11
7
19
6
12
4"""
test_input_1 = sort_nums(test_str_1)

test_str_2 = """28
33
18
42
31
14
46
20
48
47
24
23
49
45
19
38
39
11
1
32
25
35
8
17
7
9
4
2
34
10
3"""
test_input_2 = sort_nums(test_str_2)


def count_jolt_diffs(input):
    diff_ct_dict = {1: 0, 2: 0, 3: 0}

    for (i, n) in enumerate(input):
        if i == 0:
            diff_ct_dict[n] += 1

        if i == len(input) - 1:
            diff_ct_dict[3] += 1
        else:
            next = input[i + 1]
            diff_ct_dict[next - n] += 1

    print(diff_ct_dict[1] * diff_ct_dict[3])
    return diff_ct_dict


# print(count_jolt_diffs(test_input_1))  # 35
# print(count_jolt_diffs(test_input_2))  # 220
# print(count_jolt_diffs(input))  # 2059


def find_skippable(input):
    # skip1 = 0
    # skip2 = 0
    skippable = set()

    for (i, n) in enumerate(input):
        next1st = input[i + 1] if i + 1 < len(input) else None
        next2nd = input[i + 2] if i + 2 < len(input) else None

        if next2nd and next2nd <= n + 3:
            skippable.add(next1st)

    return skippable


def is_valid_skip(input, skip):
    copy = input[:]
    for n in skip:
        copy.remove(n)

    for (i, n) in enumerate(copy):
        if i == len(copy) - 1:
            continue
        else:
            next = copy[i + 1]
            if n + 3 < next:
                return False

    return True


### This works, but good luck getting it to run in a
### reasonable amount of time on anything except a supercomputer
# def count_possible_combinations(input):
#     skippable = find_skippable(input)
#     count = 0

#     for i in range(len(skippable) + 1):
#         skip_tuples = list(combinations(skippable, i))
#         # print(skip_tuples)
#         for skip in skip_tuples:
#             if is_valid_skip(input, skip):
#                 count += 1

#     return count


def count_possible_combinations(input):
    paths_in = [0] * len(input)
    paths_in[0] = 1
    for i in range(len(input)):
        for j in range(i + 1, len(input)):
            if input[j] - input[i] > 3:
                continue
            else:
                paths_in[j] += paths_in[i]

    return paths_in[-1]


print(count_possible_combinations(test_input_1))  # 8
print(count_possible_combinations(test_input_2))  # 19208
print(count_possible_combinations(input))  # 86812553324672
