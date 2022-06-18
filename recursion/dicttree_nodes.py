"""
The dict-tree consists of nested dicts.
The "edges" of the tree are ints.

Return the total "nodes" of a tree.

E.g.
Given d = {1: 11, 2: {3: 4}}
    return 5
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
# Spoiler


def f(d: dict) -> int:
    counter = 0
    for k, v in d.items():
        counter += 1
        if isinstance(v, dict):
            counter += f(v)
        else:
            counter += 1
    return counter


d = {
    'a': 1,
    'b':
        {'c':
             {'d': 2}
         },
    'e': 3
}

print(f(d))
