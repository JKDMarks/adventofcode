from pdb import set_trace as db

with open("raw-input.txt") as f:
    txt = f.read()

groups = txt.split("\n\n")


def count_groups(groups):
    count = 0
    for group in groups:
        answered = {}
        people = group.split("\n")
        for person in people:
            ans = list(person)
            for l in ans:
                answered[l] = True
        count += len(answered.keys())
    print(count)
    return count


def count_groups_2(groups):
    count = 0
    for group in groups:
        answered = {}
        people = group.split("\n")
        size = len(people)
        for person in people:
            ans = list(person)
            for l in ans:
                answered[l] = answered.get(l, 0) + 1
        for (k, v) in answered.items():
            if v == size:
                count += 1
    print(count)
    return count


count_groups(groups)
count_groups_2(groups)
