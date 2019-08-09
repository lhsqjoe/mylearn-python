# lambda 表达式
# 1. 紧跟一定的参数（如果有的话）
# 2.参数后用冒号和表达式主题隔开
# 3.只是一个表达式，所以，没有 return

stm = lambda x: 100 * x
print(stm(89))

stm2 = lambda x, y, z: x + y * 10 + z * 100
print(stm2(4, 5, 6))


# 高阶函数
# 函数名称就是一个变量
# def funA():
#     print('In funA')
#
#
# funB = funA
# funB()

def funA(n):
    return n * 100


def funB(n):
    return funA(n) * 3


print(funB(9))


# 高阶函数例子

def funC(n, f):
    return f(n) * 3


print(funC(9, funA))
