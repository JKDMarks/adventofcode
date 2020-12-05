from pdb import set_trace as db

nums = list(range(278384, 824795 + 1))


def arrayify(num):
    return [int(n) for n in str(num)]


def has_two_adj(num):
    arr = arrayify(num)
    for [i, n] in enumerate(arr):
        next = arr[i + 1] if i + 1 < len(arr) else None
        if n == next:
            return True
        else:
            continue
    return False


def has_two_adj_2(num):
    arr = arrayify(num)
    for [i, n] in enumerate(arr):
        next = arr[i + 1] if i + 1 < len(arr) else None
        next2nd = arr[i + 2] if i + 2 < len(arr) else None
        prev = arr[i - 1] if i - 1 >= 0 else None
        if n == next:
            if n == next2nd or n == prev:
                continue
            else:
                return True
        else:
            continue
    return False


def only_incr(num):
    arr = arrayify(num)
    return arr == sorted(arr)


def get_is_valid(num):
    return has_two_adj(num) and only_incr(num)


def get_is_valid_2(num):
    return has_two_adj_2(num) and only_incr(num)


count = 0  # 921
for n in nums:
    if get_is_valid(n):
        count += 1

count2 = 0  # 603
for n in nums:
    if get_is_valid_2(n):
        count2 += 1


print(count, count2)