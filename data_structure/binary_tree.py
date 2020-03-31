#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""二叉树实现练习
"""


class Node(object):

    def __init__(self, elem):
        self.elem = elem
        self.left_sub = None
        self.right_sub = None


class BinaryTree(object):

    def __init__(self):
        self.root = None

    def add(self, elem):
        if self.root is None:
            self.root = Node(elem)
            return
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            if cur.left_sub is None:
                cur.left_sub = Node(elem)
                return
            else:
                queue.append(cur.left_sub)
            if cur.right_sub is None:
                cur.right_sub = Node(elem)
                return
            else:
                queue.append(cur.right_sub)

    def breadth_travel(self):
        """广度优先遍历"""
        if self.root is None:
            return
        queue = [self.root]
        while queue:
            cur = queue.pop(0)
            print(cur.elem, end=' ')
            if cur.left_sub is not None:
                queue.append(cur.left_sub)
            if cur.right_sub is not None:
                queue.append(cur.right_sub)

    def depth_travel(self, node):
        """深度优先遍历 先序遍历
        """
        if node is None:
            return
        print(node.elem, end=' ')
        self.depth_travel(node.left_sub)
        self.depth_travel(node.right_sub)

    def mid_order(self, node):
        """深度优先遍历 中序遍历
        """
        if node is None:
            return
        self.mid_order(node.left_sub)
        print(node.elem, end=' ')
        self.mid_order(node.right_sub)

    def post_order(self, node):
        """深度优先遍历 后序遍历
        """
        if node is None:
            return
        self.post_order(node.left_sub)
        self.post_order(node.right_sub)
        print(node.elem, end=' ')


if __name__ == "__main__":
    tree = BinaryTree()
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.breadth_travel()
    print('')
    tree.depth_travel(tree.root)
    print('')
    tree.mid_order(tree.root)
    print('')
    tree.post_order(tree.root)