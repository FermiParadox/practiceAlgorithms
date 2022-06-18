"""
Given an int, return its factorial.
Try it both recursively and iteratively.
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
# Spoiler



def f(n: int) -> int:
    if n in {0, 1}:
        return 1
    return n * f(n - 1)


print(f(4))


def non_recursive(n: int) -> int:
    result = 1
    for i in range(n, 0, -1):
        result *= i

    return result


print(non_recursive(4))
