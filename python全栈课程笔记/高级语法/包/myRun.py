import sys

sys.path.append("D:\PycharmProjects\mylearn\高级语法\包")


import parent.pack2.mod2_1
import parent.pack2.mod2_2 as p2m2
from parent.pack.mod import *

if __name__ == '__main__':
    parent.pack2.mod2_1.func()

    p2m2.func()

    func()

    print('\npack2包中的模块有：')
    print(parent.pack2.__all__)


