"""
# Explain what the following code does:

                                    ((n & (n-1)) == 0).

(1) `&` = binary AND
(2) `n - 1` = subtract 1 from integer n
(3) `n & (n-1)` binary AND n & n-1
(4) `==` 0 compare to 0

Explanation: subtracts 1 from n and counts the number of `1`s n and n-1 have in common. if n and n-1 have 0 `1`s in common
return 0. n and n-1's will have 0 `1`s in common if n is a power of two. E.g.:

    n = 001000 (16)
    n -1 = 000111 (15)
    n & n = 0

"""


