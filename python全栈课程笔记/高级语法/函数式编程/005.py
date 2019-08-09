#  装饰器
import time


def printTime(f):
    def wrpper(*args, **kwargs):
        print('Time: ', time.ctime())
        return f(*args, **kwargs)

    return wrpper


@printTime
def hello():
    print('Hello world!')


hello()

print('---------------------------------------')


def hello2():
    print('Hello world!222')


f = printTime(hello2)  # 手动执行
f()

print('---------------------------------------')

import collections

Point = collections.namedtuple('Point', ['x', 'y'])
p = Point(11, 22)
print(p.x)
print(p[0])

Circle = collections.namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(100, 150, 50)
print(c)
print(type(c))

print(isinstance(c, tuple))  # True
