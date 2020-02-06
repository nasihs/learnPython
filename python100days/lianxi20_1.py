"""
@property装饰器
加入ValueError检测
"""


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise ValueError('width must be an integer')
        if value < 0 or value > 2000:
            raise ValueError('width must between 0~2000')
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

    @property
    def resolution(self):
        return self._width * self._height


def main():
    s1 = Screen()
    s1.width = 1920
    s1.height = 1080
    print(s1.width)
    print(s1.height)
    print(s1.resolution)


if __name__ == '__main__':
    main()
