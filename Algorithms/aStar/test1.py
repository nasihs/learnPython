from math import sqrt
from heapq import heappop, heappush
# import matplotlib as plt

#open_list = [(1, 1), (2, 2), (3, 3)]
open_list = []
closed_list = []
# start_point = (0, 0)
# goal_point = (5, 6)
OBSTACLE = [(3, y) for y in range(1, 5)]
BORDER = [(x, 0) for x in range(8)] + [(x, 7) for x in range(8)] + [(0, y) for y in range(8)] + [(7, y) for y in range(8)]
DIRECTIONS = ((-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (1, 0), (1, -1))
parent_node = {}
g_score = {}
f_score = {}
path = []


class Node(object):
    def __init__(self, coordinates):
        self._x = coordinates[0]
        self._y = coordinates[1]
        self._coord = coordinates

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

    # def is_in_open(self):
    """ def search_adjacent_node(self):
        for direction in DIRECTIONS:
            self._x """
    @property
    def g_score(self):
        return g_score[self.coord]

    @g_score.setter
    def g_score(self, value):
        g_score[self.coord] = value

    @property
    def h_score(self):
        return 0
        #return sqrt((self._x - another.x)**2 + (self._y - another.y)**2)

    @property
    def f_score(self):
        return self.g_score + self.h_score


def dist_between(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)





def main():
    n1 = Node((1, 1))
    n2 = Node((2, 2))
    n3 = Node((3, 3))
    heappush(open_list, n1.coord)
    heappush(open_list, n2.coord)
    heappush(open_list, n3.coord)
    # open_list.append(n1.coord)
    n1.g_score = 2
    n2.g_score = 3
    n3.g_score = 1
    print(open_list)
    print(g_score)
    open_list.sort(key=lambda point: Node((point)).f_score)
    print(open_list)
    print(open_list[0])
    heappop(open_list)
    print(open_list)


if __name__ == '__main__':
    main()
