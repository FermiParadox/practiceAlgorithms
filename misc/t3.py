import collections

Point = collections.namedtuple('Point', ['left', 'right', 'value'])


def is_inside(root: Point, value: int) -> bool:
    if root.value == value:
        return True
    else:
        try:
            if root.value > value:
                return is_inside(root.left, value)
            elif root.value < value:
                return is_inside(root.right, value)
        except AttributeError:
            pass
    return False


n1 = Point(value=1, left=None, right=None)
n3 = Point(value=3, left=None, right=None)
n2 = Point(value=2, left=n1, right=n3)
print(is_inside(n2, 3))

n1 = Point(value=1, left=None, right=None)
n3 = Point(value=3, left=None, right=None)
n2 = Point(value=2, left=n1, right=n3)
print(is_inside(n2, 4))
