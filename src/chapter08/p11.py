"""
Coins: Given an infinite number of quarters (25 cents), dimes (10 cents), nickels (5 cents), and
pennies (1 cent), write code to calculate the number of ways of representing n cents.
"""


def number_of_ways_to_represent_n_cents(n: int):
    available_cents = [25, 10, 5, 1]
    memo: list = [0] * (n + 1)  # noqa
    memo[0] = 1
    for i in range(0, len(available_cents)):
        for j in range(available_cents[i], n + 1):
            memo[j] += memo[j - available_cents[i]]
    return memo[n]
