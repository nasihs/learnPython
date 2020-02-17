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
        g_score[self.coord] = value.coord

    @property
    def h_score(self):
        return sqrt((self._x - goal_node.x)**2 + (self._y - goal_node.y)**2)

    @property
    def f_score(self):
        return self.g_score + self.h_score


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
        heappop(open_list)
        heappush(closed_list, current_node.coord)
        for direction in DIRECTIONS:
            x = current_node.x + direction[0]
            y = current_node.y + direction[1]
            next_node = Node((x, y))
            if next_node.coord in closed_list:
                continue
            elif next_node.coord in OBSTACLE:
                continue
            elif next_node in BORDER:
                continue
            elif next_node not in open_list:
                heappush(open_list, next_node.coord)
                next_node.parent = current_node
            


def main():
    

   


if __name__ == '__main__':
    main()
