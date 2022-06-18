"""
Given an int, return it's fibonacci.
"""


# Spoiler
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
# Spoiler

def f(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1

    return f(n - 2) + f(n - 1)


print(f(10))
