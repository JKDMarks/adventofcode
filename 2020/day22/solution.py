from pdb import set_trace as db

with open("input.txt") as f:
    decks_str = f.read()

test_decks_str = """Player 1:
9
2
6
3
1

Player 2:
5
8
4
7
10"""


def make_decks(decks_str):
    return [[int(n) for n in deck.splitlines()[1:]] for deck in decks_str.split("\n\n")]


def calc_score(winner):
    score = 0
    for i in range(len(winner)):
        score += winner[i] * (len(winner) - i)

    return score


def play(deck1, deck2):
    while len(deck1) > 0 and len(deck2) > 0:
        c1 = deck1.pop(0)
        c2 = deck2.pop(0)

        if c1 > c2:
            deck1 += [c1, c2]
        else:
            deck2 += [c2, c1]

    return 1 if len(deck1) > 0 else 2


def run_p1(decks_str):
    deck1, deck2 = make_decks(decks_str)
    winner = play(deck1, deck2)
    return calc_score(deck1) if winner == 1 else calc_score(deck2)


print(run_p1(test_decks_str))  # 306
print(run_p1(decks_str))  # 32783
