from functools import reduce
from pdb import set_trace as db

with open("input.txt") as f:
    foods = f.read().splitlines()

test_foods = """mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)""".splitlines()


def match_allergens(foods, is_p1=False):
    foods = [
        [set(i.split()), set(a.replace(",", "").split())]
        for i, a in [food[:-1].split(" (contains ") for food in foods]
    ]

    possible = {}
    ingr_usage = []
    all_ingrs = set()
    for ingrs, allgs in foods:
        ingr_usage += ingrs
        all_ingrs |= ingrs

        for allg in allgs:
            if allg not in possible:
                possible[allg] = ingrs.copy()
            else:
                possible[allg] &= ingrs

    if is_p1:
        possible_allergens = reduce(lambda a, b: a | b, possible.values())
        not_possible_allergens = all_ingrs - possible_allergens
        return sum(ingr_usage.count(ingr) for ingr in not_possible_allergens)

    allg_ingr = {}
    while any(len(v) for v in possible.values()):
        for allg, ingrs in possible.items():
            if len(ingrs) == 1:
                ingr = min(ingrs)
                allg_ingr[allg] = ingr
                for rem_ingrs in possible.values():
                    if ingr in rem_ingrs:
                        rem_ingrs.remove(ingr)

    return ",".join([allg_ingr[k] for k in sorted(allg_ingr.keys())])


print(match_allergens(test_foods, True))  # 5
print(match_allergens(foods, True))  # 2627

print(match_allergens(test_foods))  # mxmxvkd,sqjhc,fvjkl
# mxmxvkd contains dairy.
# sqjhc contains fish.
# fvjkl contains soy.

print(match_allergens(foods))  # hn,dgsdtj,kpksf,sjcvsr,bstzgn,kmmqmv,vkdxfj,bsfqgb
