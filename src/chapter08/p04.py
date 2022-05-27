"""
**Power Set:**

Write a method to return all subsets of a set.
"""


def get_all_subsets_of_set_suffix_solution(universe: list) -> list[list]:
    size = len(universe)
    memo: list[list] = [None] * size  # noqa
    # base case
    for i in range(size):
        memo[i] = [[universe[i]]]

    for i in reversed(range(size - 1)):
        for j in memo[i + 1]:
            memo[i].append([universe[i]] + j)
        memo[i].extend(memo[i + 1])

    return memo


def get_all_subsets_of_sets_substring_solution(universe: list) -> list[list]:
    size = len(universe)
    memo: list[list] = [None] * size  # noqa
    # base case
    for i in range(size):
        memo[i] = [[universe[i]]]

    for i in reversed(range(size)):
        for j in range(i + 1, size):
            for ss in memo[j]:
                memo[i].append([universe[i]] + ss)

    return memo
