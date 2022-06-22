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


p1 = Point(value=1, left=None, right=None)
p3 = Point(value=3, left=None, right=None)
p2 = Point(value=2, left=p1, right=p3)
print(is_inside(p2, 3))

p1 = Point(value=1, left=None, right=None)
p3 = Point(value=3, left=None, right=None)
p2 = Point(value=2, left=p1, right=p3)
print(is_inside(p2, 4))
