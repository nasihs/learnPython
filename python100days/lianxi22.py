"""
静态方法
"""

from math import sqrt


class Triangle(object):

    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and b + c > a and c + a > b

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        p = self.perimeter() / 2
        return sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))


def main():
    a, b, c = 3, 4, 5
    # 静态方法和类方法都是通过给类发消息来调用
    if Triangle.is_valid(a, b, c):
        t1 = Triangle(a, b, c)
        print(t1.perimeter())
        # 也可以通过给类发送消息来调用对象方法
        # 但是要传入接收消息的对象作为参数
        print(t1.area())
        # print(Triangle.area(t1))
    else:
        print('无法构成三角形')


if __name__ == '__main__':
    main()
