"""
三角形周长&面积计算
"""

a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
if a + b > c and b + c > a and c + a > b:
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c))**0.5
    print('周长=%.1f' % (a + b + c))
    print('面积=%f' % area)
else:
    print('非三角形')
