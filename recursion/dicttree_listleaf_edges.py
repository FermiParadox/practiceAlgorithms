"""
The dict-tree consists of nested dicts.
The "edges" of the tree are lists of ints.

Return all edges as a list.
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
# Spoiler

d = {
    'a': [1, 2],
    'b':
        {'c':
             {'d': [3, 4, 5]}
         },
    'e': [6, 7]
}


def f(tree: dict) -> list:
    l = []
    for k, v in tree.items():
        if isinstance(v, dict):
            l += f(v)
            continue
        l += v
    return l


print(f(d))
