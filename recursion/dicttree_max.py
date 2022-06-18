"""
The dict-tree consists of nested dicts.
The keys and values of the tree are ints.

Return the max int.
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
    6: 3,
    2:
        {1:
             {19: 221}
         },
    11: 8
}


def f(d: dict) -> int:
    m = 0

    for k, v in d.items():
        if isinstance(k, int):
            m = max(k, m)
        if isinstance(v, int):
            m = max(v, m)
        else:
            m = max(f(v), m)

    return m


print(f(d))
