"""
英制单位英寸和公制单位厘米互换
"""

value = float(input('请输入长度：'))
unit = input('请输入单位：')
if unit == 'cm':
    print('%f厘米=%.1f英寸' % (value, value * 2.54))
elif unit == 'inch':
    print('%f英寸=%.1f厘米' % (value, value / 2.54))
else:
    print('请输入正确的单位')
