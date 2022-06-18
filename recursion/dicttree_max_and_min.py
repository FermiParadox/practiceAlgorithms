"""
The dict-tree consists of nested dicts.
The keys and values of the tree are ints.
Ints from 0 to 1000.

Return the max int and min.
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
# Spoiler
from typing import List

d = {
    6: 3,
    2:
        {1:
             {19: 221}
         },
    11: 8
}


def f(given_dict: dict) -> List[int]:
    m = 1000
    M = 0
    for k, v in given_dict.items():
        if isinstance(k, int):
            m = min(m, k)
            M = max(M, k)
        if isinstance(v, int):
            m = min(m, v)
            M = max(M, v)
        else:
            temp_list = f(v)
            m = min(m, temp_list[0])
            M = max(M, temp_list[1])

    return [m, M]


print(f(d))
