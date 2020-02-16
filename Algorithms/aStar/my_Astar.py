from math import sqrt
# import matplotlib as plt

open_list = []
closed_list = []
start_point = (0, 0)
end_point = (5, 6)
OBSTACLE = [(3, y) for y in range(1, 5)]
BORDER = [(x, 0) for x in range(7)] + [(0, y) for y in range(7)]
DIRECTIONS = ((-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (1, 0), (1, -1))
parent_node = {}
route = []


class Node(object):
    def __init__(self, coordinates, parent=None):
        self._x = coordinates[0]
        self._y = coordinates[1]
        self._coord = coordinates
        parent_node[coordinates] = parent

    def __str__(self):
        return '(%s, %s)' % (str(self._x), str(self._y))

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def coord(self):
        return self._coord

    @property
    def parent(self):
        return parent_node[self._coord]

    @parent.setter
    def parent(self, value):
        parent_node[self._coord] = value

    #def is_border(self):

    #def is_obstacle(self):

    # def is_in_open(self):


    def calc_g(self, another):
        return abs(self._x - another.x) + abs(self._y - another.y)

    def calc_h(self, another):
        return sqrt((self._x - another.x)**2 + (self._y - another.y)**2)

    def calc_f(self, another):
        return another.get_g(another) + another.get_h(another)


def main():
    n1 = Node((1, 0))
    n2 = Node((5, 6))
    print(n1)
    print('the parent of n2 is:', n2.parent)
    n2.parent = n1.coord
    print('the parent of n2 is:', n2.parent)
    print('the coordinates of n2 is:', n2.coord)
    print('the x coordinates of n2 is:', n2.coord[0])
    



if __name__ == '__main__':
    main()
