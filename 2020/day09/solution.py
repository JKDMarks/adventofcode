from pdb import set_trace as db

with open("raw-input.txt") as f:
    input = [int(n) for n in f.read().split("\n")]

test_str = """35
20
15
25
47
40
62
55
65
95
102
117
150
182
127
219
299
277
309
576"""
test_input = [int(n) for n in test_str.split("\n")]


def check_is_valid(chunk, num):
    for (i, a) in enumerate(chunk):
        for b in chunk[i + 1 :]:
            if num == a + b:
                return True
    return False


def find_first_invalid(input, chunk_size):
    chunk = input[:chunk_size]
    i = chunk_size
    while i < len(input):
        curr = input[i]
        if not check_is_valid(chunk, curr):
            return curr
        chunk.pop(0)
        chunk.append(curr)
        i += 1


print(find_first_invalid(test_input, 5))  # 127
print(find_first_invalid(input, 25))  # 167829540

### BRUTE FORCE
# def find_weakness(input, tgt_num):
#     for (i, a) in enumerate(input):
#         for (j, b) in enumerate(input[i + 1 :]):
#             weak_arr = input[i : i + j + 1]
#             arr_sum = sum(weak_arr)
#             if arr_sum > tgt_num:
#                 break
#             elif arr_sum == tgt_num:
#                 print(weak_arr)
#                 return min(weak_arr) + max(weak_arr)

### ROLLING SUM
def find_weakness(input, tgt_num):
    start_i = 0
    end_i = 1
    arr_sum = sum(input[start_i : end_i])
    while end_i < len(input):
        if arr_sum == tgt_num:
            break
        elif arr_sum < tgt_num:
            arr_sum += input[end_i]
            end_i += 1
        elif arr_sum > tgt_num:
            arr_sum -= input[start_i]
            start_i += 1

    sub_arr = input[start_i : end_i]
    return min(sub_arr) + max(sub_arr)


print(find_weakness(test_input, 127))  # 62
print(find_weakness(input, 167829540))  # 28045630
