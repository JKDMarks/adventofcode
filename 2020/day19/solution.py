import re
from pdb import set_trace as db

with open("raw-input.txt") as f:
    txt = f.read()

test_txt = """0: 4 1 5
1: 2 3 | 3 2
2: 4 4 | 5 5
3: 4 5 | 5 4
4: "a"
5: "b"

ababbb
bababa
abbbab
aaabbb
aaaabbb"""

test_txt_2 = """42: 9 14 | 10 1
9: 14 27 | 1 26
10: 23 14 | 28 1
1: "a"
11: 42 31
5: 1 14 | 15 1
19: 14 1 | 14 14
12: 24 14 | 19 1
16: 15 1 | 14 14
31: 14 17 | 1 13
6: 14 14 | 1 14
2: 1 24 | 14 4
0: 8 11
13: 14 3 | 1 12
15: 1 | 14
17: 14 2 | 1 7
23: 25 1 | 22 14
28: 16 1
4: 1 1
20: 14 14 | 1 15
3: 5 14 | 16 1
27: 1 6 | 14 18
14: "b"
21: 14 1 | 1 14
25: 1 1 | 1 14
22: 14 14
8: 42
26: 14 22 | 1 20
18: 15 15
7: 14 5 | 1 21
24: 14 1

abbbbbabbbaaaababbaabbbbabababbbabbbbbbabaaaa
bbabbbbaabaabba
babbbbaabbbbbabbbbbbaabaaabaaa
aaabbbbbbaaaabaababaabababbabaaabbababababaaa
bbbbbbbaaaabbbbaaabbabaaa
bbbababbbbaaaaaaaabbababaaababaabab
ababaaaaaabaaab
ababaaaaabbbaba
baabbaaaabbaaaababbaababb
abbbbabbbbaaaababbbbbbaaaababb
aaaaabbaabaaaaababaa
aaaabbaaaabbaaa
aaaabbaabbaaaaaaabbbabbbaaabbaabaaa
babaaabbbaaabaababbaabababaaab
aabbbbbaabbbaaaaaabbbbbababaaaaabbaaabba"""


def parse_line(line):
    rule_num, tgt_str = line.split(": ")
    if '"' in tgt_str:
        return (int(rule_num), tgt_str[1])
    else:
        return (
            int(rule_num),
            [[int(r) for r in tgt.split(" ")] for tgt in tgt_str.split(" | ")],
        )


def make_rules(rules_txt, is_p2):
    rules = dict([parse_line(line) for line in rules_txt.splitlines()])
    if is_p2:
        rules[8] = [[42], [42, 8]]
        rules[11] = [[42, 31], [42, 11, 31]]

    return rules


def solve(rules, msg_str, seq):
    if msg_str == "" or seq == []:
        return msg_str == "" and seq == []

    rule = rules[seq[0]]
    # print(msg_str, seq, r)
    if type(rule) == str:
        if msg_str[0] == rule:
            return solve(rules, msg_str[1:], seq[1:])
        else:
            return False

    else:
        return any(solve(rules, msg_str, seq_option + seq[1:]) for seq_option in rule)


def count_valid(txt, is_p2=False):
    rules_txt, msgs = txt.split("\n\n")
    rules = make_rules(rules_txt, is_p2)

    return sum(solve(rules, msg, [0]) for msg in msgs.split("\n"))


print(count_valid(test_txt))  # 2
print(count_valid(txt))  # 299

print(count_valid(test_txt_2))  # 3
print(count_valid(test_txt_2, True))  # 12
print(count_valid(txt, True))  # 414
