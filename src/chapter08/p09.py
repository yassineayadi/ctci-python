"""
Parens: Implement an algorithm to print all valid (e.g., properly opened and closed) combinations
of n pairs of parentheses.
"""


def get_pairs_of_parens(n: int):
    memo: list[list[str]] = [None] * (n + 1)  # noqa
    memo[n], memo[n - 1] = [], ["()"]

    for i in reversed(range(n -1)):
        parens = []
        for previous in memo[i + 1]:
            left = "()" + previous
            right = previous + "()"
            around = "(" + previous + ")"
            if left == right:
                parens.extend([left, around])
            else:
                parens.extend([left, right, around])
        memo[i] = parens
    return memo[0]
