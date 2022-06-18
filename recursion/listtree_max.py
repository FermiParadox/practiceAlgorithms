"""
The list-tree consists of nested lists.
The "edges" of the tree are ints or lists of ints. All positive.

Return the max.

E.g.
given: [1, 2, [3, 4, [5, 6, 7]], [8, 9]]
    return 9
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
# Spoiler

l = [1, 2, [3, 4, [5, 6, 7]], [8, 9]]


def f(given_list: list) -> list:
    m = 0
    for i in given_list:
        if isinstance(i, list):
            m = max(f(i), m)
        else:
            m = max(i, m)
    return m


print(f(l))
