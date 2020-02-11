"""使用turtle绘图"""
from turtle import *


def draw_heart(x, y, size):
    penup()
    goto(x, y)
    pendown()
    color('pink')
    begin_fill()
    # right(90)
    setheading(135)
    fd(size * 2)
    circle(-size, 180)
    left(90)
    circle(-size, 180)
    fd(size * 2)
    end_fill()


def setting():
    title('luckypot')
    setup(width=900, height=500)
    hideturtle()
    # color('pink')
    pensize(4)
    speed(10)


def main():
    setting()
    write('luckyp  t',
          move=False,
          align="center",
          font=("Microsoft YaHei", 160, "normal"))
    draw_heart(290, 50, 35)
    done()


if __name__ == '__main__':
    main()
