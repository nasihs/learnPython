from math import sqrt
from heapq import heappop, heappush
# import matplotlib as plt

open_list = []
closed_list = []
# start_point = (0, 0)
# goal_point = (5, 6)
OBSTACLE = [(3, y) for y in range(1, 5)]
BORDER = [(x, 0) for x in range(8)] + [(x, 7) for x in range(8)] + [
    (0, y) for y in range(8)
] + [(7, y) for y in range(8)]
DIRECTIONS = ((-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (1, 0), (1,
                                                                           -1))
parent_node = {}
g_list = {}
f_list = {}
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
        parent_node[self._coord] = value.coord

    # def is_in_open(self):
    @property
    def g_score(self):
        return g_list[self._coord]

    @g_score.setter
    def g_score(self, value):
        #g_list[self._coord] = g_list[self.parent] + dist_between(self._coord, self.parent)
        g_list[self._coord] = value

    """(6, 3)终点坐标 用global申明还是报undefined"""
    @property
    def h_score(self):
        return sqrt((self._x - 6)**2 + (self._y - 3)**2)

    @property
    def f_score(self):
        f_list[self._coord] = self.g_score + self.h_score
        return f_list[self._coord]


def dist_between(a, b):
    return sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)


def a_star(start, goal):
    start_node = Node(start)
    goal_node = Node(goal)
    start_node.g_score = 0
    # open_list.add(current_node)
    heappush(open_list, start_node.coord)
    # current_node = start_node.coord


def main():
    start = (1, 3)
    goal = (6, 3)
    start_node = Node(start)
    start_node.g_score = 0
    print(g_list)
    print(start_node.f_score)
    n1 = Node((2, 4))
    n1.parent = start_node
    n1.g_score = 



if __name__ == '__main__':
    main()
