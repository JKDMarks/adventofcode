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
            ans = [l for l in person]
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
            ans = [l for l in person]
            for l in ans:
                if l in answered:
                    answered[l] += 1
                else:
                    answered[l] = 1
        for (k, v) in answered.items():
            if v == size:
                count += 1
    print(count)
    return count


count_groups(groups)
count_groups_2(groups)
