"""
面向对象编程
"""


class Student(object):

    # __init__是一个特殊方法用于在创建对象时进行初始化操作
    # 通过这个方法我们可以为Student对象绑定name和age两个属性
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self, course_name):
        print('%s正在学习%s.' % (self.name, course_name))

    # PEP8要求标识符的名字用全小写多个单词用下划线连接
    # 但是部分程序员和公司更倾向于使用驼峰命名法
    def watch_movie(self):
        if self.age < 18:
            print('%s只能观看《熊出没》.' % self.name)
        else:
            print('%s正在观看123.' % self.name)


def main():
    # 创建Student对象并指定姓名和年龄
    stu1 = Student('十三', 13)
    # 给对象发study消息
    stu1.study('Python程序设计')
    stu1.watch_movie()


if __name__ == '__main__':
    main()
