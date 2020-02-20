from math import sqrt
from heapq import heappop, heappush
# import matplotlib as plt

open_list = []
closed_list = []
# start_point = (0, 0)
# goal_point = (5, 6)
OBSTACLE = [(3, y) for y in range(1, 5)]
BORDER = [(x, 0) for x in range(8)] + [(x, 7) for x in range(8)] + [(0, y) for y in range(8)] + [(7, y) for y in range(8)]
DIRECTIONS = ((-1, 1), (0, 1), (1, 1), (-1, 0), (1, 0), (-1, -1), (1, 0), (1, -1))
parent_node = {}
g_list = {}
f_list = {}
path = []


class Node(object):
    def __init__(self, coordinates):
        self._x = coordinates[0]
        self._y = coordinates[1]
        self._coord = coordinates
        self._g_score = g_list[self.parent] + dist_between(coordinates, parent_node[coordinates])

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
        #return g_list[self._coord]
        return self._g_score

    @g_score.setter
    def g_score(self, value):
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
    while open_list:
        open_list.sort(key=lambda node: Node((node)).f_score)
        current_node = Node(open_list[0])
        if current_node.coord == goal_node.coord:
            print('Path is found.')
            return
        heappop(open_list)
        heappush(closed_list, current_node.coord)
        for direction in DIRECTIONS:
            x = current_node.x + direction[0]
            y = current_node.y + direction[1]
            next_node = Node((x, y))
            if next_node.coord in closed_list:
                continue
            if next_node.coord in OBSTACLE:
                continue
            if next_node in BORDER:
                continue
            #next_node.g_score = Node(next_node.parent).g_score + dist_between(next_node.coord, next_node.parent)
            if next_node not in open_list:
                heappush(open_list, next_node.coord)
                next_node.parent = current_node
            else:
                if current_node.g_score + dist_between(current_node.coord, next_node.coord) < next_node.g_score:
                    next_node.parent = current_node
                    next_node.g_score = current_node.g_score + dist_between(current_node.coord, next_node.coord)
                    next_node.f_score
    print('Failed.')


def main():
    start = (1, 3)
    goal = (6, 3)
    a_star(start, goal)


if __name__ == '__main__':
    main()
