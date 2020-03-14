#!/usr/bin/python3
# -*- coding: utf-8 -*-


"""单链表
"""


class Node(object):

    def __init__(self, elem):
        self.elem = elem
        self.next = None


class SinglyLinkedList(object):

    def __init__(self):
        self.__head = None

    def is_empty(self):
        return self.__head is None

    def length(self):
        cur = self.__head
        len = 0
        while cur is not None:
            len += 1
            cur = cur.next
        return len

    def travel(self):
        cur = self.__head
        while cur is not None:
            print(cur.elem, end=' ')
            cur = cur.next
        print('')

    def add(self, elem):
        node = Node(elem)
        node.next = self.__head
        self.__head = node

    def append(self, elem):
        cur = self.__head
        if self.length() == 0:
            self.add(elem)
        else:
            while cur.next is not None:
                cur = cur.next
            node = Node(elem)
            cur.next = node

    def insert(self, elem, pos):
        cur = self.__head
        prev = None
        if pos < 0 or pos > self.length() - 1:
            print('pos is out of range.')
        elif pos == 0:
            self.add(elem)
        elif pos == self.length() - 1:
            self.append(elem)
        else:
            i = 0
            while i < pos:
                i += 1
                prev = cur
                cur = cur.next
            node = Node(elem)
            node.next = cur
            prev.next = node

    def search(self, elem):
        cur = self.__head
        while cur is not None:
            if cur.elem == elem:
                return True
            cur = cur.next
        return False
        
    def remove(self, pos):
        # 删除指定位置
        cur = self.__head
        prev = None
        if pos < 0 or pos > self.length() - 1:
            print('pos is out of range.')
        elif pos == 0:
            self.__head = self.__head.next
        else:
            i = 0
            while i < pos:
                i += 1
                prev = cur
                cur = cur.next
            prev.next = cur.next


if __name__ == '__main__':
    list = SinglyLinkedList()
    print(list.is_empty())
    list.add(1)
    list.add(2)
    list.add(3)
    list.travel()
    # print(list.length())
    list.append(0)
    list.travel()
    # print(list.length())
    list.insert(33, 2)
    list.travel()
    # print(list.length())
    print(list.search(3))
    print(list.search(22))
    list.remove(2)
    list.travel()
