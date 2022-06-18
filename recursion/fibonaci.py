"""
Given an int, return it's fibonaci.
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

    return n + f(n-1)


print(f(10))
