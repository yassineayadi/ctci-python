"""
Boolean Evaluation: Given a boolean expression consisting of the symbols 0 (false), 1 (true), &
(AND), | (OR), and ^ (XOR), and a desired boolean result value result, implement a function to
count the number of ways of parenthesizing the expression such that it evaluates to result.
"""

from operator import and_ as b_and, or_ as b_or, xor as b_xor


def boolean_parenthesization(values: list[int], operators: list[callable]):
    size = len(values)
    memo: list[list[list[int]]] = [  # noqa
        [[None] * 2 for _ in range(size)] for _ in range(size)
    ]

    # base case
    for i in range(size):
        if values[i] == 0:
            memo[i][i][0] = 1
            memo[i][i][1] = 0
        else:
            memo[i][i][0] = 0
            memo[i][i][1] = 1

    for i in reversed(range(size)):
        for j in range(i + 1, size):
            for k in range(i, j):
                operator = operators[k]
                left_zeros_count, right_zeros_count = memo[i][k][0], memo[k + 1][j][0]
                left_ones_count, right_ones_count = memo[i][k][1], memo[k + 1][j][1]
                if operator is b_xor:
                    zeros_count = (left_ones_count * right_ones_count) + (
                        left_zeros_count * right_zeros_count
                    )
                    ones_count = (left_zeros_count * right_ones_count) + (
                        left_ones_count * right_zeros_count
                    )
                elif operator is b_and:
                    zeros_count = (
                        (left_zeros_count * right_ones_count)
                        + (left_zeros_count * right_zeros_count)
                        + (right_zeros_count * left_ones_count)
                    )
                    ones_count = left_ones_count * right_ones_count
                # b_or
                else:
                    zeros_count = left_zeros_count * right_zeros_count
                    ones_count = (
                        (left_ones_count * right_zeros_count)
                        + (right_ones_count * left_ones_count)
                        + (right_ones_count * left_zeros_count)
                    )

                if memo[i][j][0] is not None:
                    current_max_zeros_count = memo[i][j][0]
                else:
                    current_max_zeros_count = 0
                if memo[i][j][1] is not None:
                    current_max_ones_count = memo[i][j][1]
                else:
                    current_max_ones_count = 0

                memo[i][j][0] = max(zeros_count, current_max_zeros_count)
                memo[i][j][1] = max(ones_count, current_max_ones_count)

    return memo[0][size - 1][0], memo[0][size - 1][1]
