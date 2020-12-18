import re
from pdb import set_trace as db
from functools import reduce

with open("raw-input.txt") as f:
    homework = f.read().split("\n")


ex1 = "1 + 2 * 3 + 4 * 5 + 6"
ex2 = "1 + (2 * 3) + (4 * (5 + 6))"
ex3 = "2 * 3 + (4 * 5)"
ex4 = "5 + (8 * 3 + 9 + 3 * 4 * 3)"
ex5 = "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))"
ex6 = "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"


def eval(expr_str):
    expr = expr_str.split(" ")
    a, op, b = expr[:3]
    rest = " " + " ".join(expr[3:]) if expr[3:] else ""

    if op == "+":
        return str(int(a) + int(b)) + rest
    elif op == "*":
        return str(int(a) * int(b)) + rest


def solve_expr(expr):
    if (
        expr.startswith("(")
        and expr.endswith(")")
        and not re.match(r"\(.*\(.*\)", expr)
    ):
        while "+" in expr or "*" in expr:
            expr = expr[1:-1]
            expr = "(" + eval(expr) + ")"

        expr = expr[1:-1]
        return expr
    else:
        paren_exprs = re.findall(r"(\([\d*+ ]+\))", expr)

        while paren_exprs:
            for paren_expr in paren_exprs:
                expr = expr.replace(paren_expr, solve_expr(paren_expr))
            paren_exprs = re.findall(r"(\([\d*+ ]+\))", expr)

        while "+" in expr or "*" in expr:
            expr = eval(expr)

    return expr


# print(solve_expr(ex1))  # 71
# print(solve_expr(ex2))  # 51
# print(solve_expr(ex3))  # 26
# print(solve_expr(ex4))  # 437
# print(solve_expr(ex5))  # 12240
# print(solve_expr(ex6))  # 13632
# print(solve_expr("(2 * 2 + 2 + 7 * 3 + 3) + (3 + (5 + 2 * 2 + 8 * 5))"))


def solve_homework(homework):
    total = 0

    for expr in homework:
        total += int(solve_expr(expr))

    return total


print(solve_homework(homework))  # 12956356593940


def true_eval(expr_str):
    expr = expr_str.split(" ")
    a, op, b = expr[:3]
    rest = " " + " ".join(expr[3:]) if expr[3:] else ""

    if op == "+":
        return str(int(a) + int(b)) + rest
    elif op == "*":
        return str(int(a) * int(b)) + rest


def true_solve_expr(expr):
    if expr.count("+") + expr.count("*") > 1:
        expr = re.sub(r"(\d+ \+ \d+)", r"(\1)", expr)

    if (
        expr.startswith("(")
        and expr.endswith(")")
        and not re.match(r"\(.*\(.*\)", expr)
    ):
        while "+" in expr or "*" in expr:
            expr = expr[1:-1]
            expr = "(" + true_eval(expr) + ")"
            if expr.count("+") + expr.count("*") > 1:
                expr = re.sub(r"(\d+ \+ \d+)", r"(\1)", expr)

        expr = expr[1:-1]
        return expr
    else:
        paren_exprs = re.findall(r"(\([\d*+ ]+\))", expr)

        while paren_exprs:
            for paren_expr in paren_exprs:
                expr = expr.replace(paren_expr, true_solve_expr(paren_expr))
                expr = re.sub(r"(\d+ \+ \d+)", r"(\1)", expr)

            paren_exprs = re.findall(r"(\([\d*+ ]+\))", expr)

        while "+" in expr or "*" in expr:
            expr = true_eval(expr)

    return expr


# print(true_solve_expr(ex3))  # 46
# print(true_solve_expr(ex4))  # 1445
# print(true_solve_expr(ex5))  # 669060
# print(true_solve_expr(ex6))  # 23340


def true_solve_homework(homework):
    total = 0

    for expr in homework:
        total += int(true_solve_expr(expr))

    return total


print(true_solve_homework(homework))  # 94240043727614