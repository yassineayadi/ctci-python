"""
**Triple Step:**

A child is running up a staircase with n steps and can hop either 1 step, 2 steps, or 3 steps at a time.
Implement a method to count how many possible ways the child can run up the stairs.
"""


def count_possible_ways(stairs: int):
    memo: list[int] = [None for _ in range(10 + 1)]  # noqa
    memo[0] = 0
    memo[1] = 1
    memo[2] = 3
    for i in range(3, stairs + 1):
        memo[i] = memo[i - 1] + memo[i - 2] + memo[i - 3]
    return memo[stairs]
