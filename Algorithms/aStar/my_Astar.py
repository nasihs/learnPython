from math import sqrt
# import matplotlib as plt

open_set = []
closed_set = []
DIRECTIONS = []


class Node(object):
    def __init__(self, coordinates, parent=None):
        self._x = coordinates[0]
        self._y = coordinates[1]
        self._parent = parent

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def parent(self):
        return self._parent

    @parent.setter
    def parent(self, value):
        self._parent = value

    def get_g(self, another):
        return abs(self._x - another.x) + abs(self._y - another.y)
    
    def get_h(self, another):
        return sqrt((self._x - another.x)**2 + (self._y - another.y)**2)

    def get_f(self, another):
        return another.get_g(another) + another.get_h(another)


def main():
    n1 = Node((0, 0))
    n2 = Node((2, 1))
    print(n1.get_f(n2))


if __name__ == '__main__':
    main()
