"""
??@property???
"""


class Screen(object):
    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
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
    s1.width = float(input('输入width:'))
    s1.height = float(input('输入height:'))
    print(s1.width)
    print(s1.height)
    print(s1.resolution)


if __name__ == '__main__':
    main()
