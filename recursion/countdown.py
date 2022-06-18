"""
Countdown:

given n = 4,
    return [4, 3, 2, 1, 0]
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


def f(n: int) -> list:
    if n == 0:
        return [0]

    return [n, ] + f(n - 1)


print(f(10))
