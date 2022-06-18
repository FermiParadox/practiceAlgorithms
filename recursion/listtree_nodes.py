"""
The list-tree consists of nested lists.
The "edges" of the tree are ints or lists of ints.

Return all elements as a list.

E.g.
given: [1, 2, [3, 4, [5, 6, 7]], [8, 9]]
    return [1,2,3,4,5,6,7,8,9]
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
    result = []
    for i in given_list:
        if isinstance(i, list):
            result += f(i)
        else:
            result.append(i)
    return result


print(f(l))
