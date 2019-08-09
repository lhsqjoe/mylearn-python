# 直接使用生成器
L = [x * x for x in range(5)]  # 列表生成器
g = (x * x for x in range(5))  # 生成器
print(type(g))  # <class 'generator'>  生成器类型
print(type(L))  # <class 'list'>


# 函数案例
# def odd():
#     print('Step 1')
#     print('Step 2')
#     print('Step 3')
#     return None
#
#
# odd()

# 生成器案例
# 在函数odd中， yield 负责返回(可以看作是return 吧)
def odd():
    print('Step 1')
    yield 1
    print('Step 2')
    yield 1
    print('Step 3')
    yield 1


# odd()  # 这么调用是不行的


one = odd()
print(next(one))
print(next(one))
print(next(one))

# for 循环调用生成器


# def fib(max):
#     n, a, b, = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n += 1
#     return None
#
#
# fib(5)
print('-------------------------------')


def fib(max):
    n, a, b, = 0, 0, 1
    while n < max:
        # print(b)
        yield b
        a, b = b, a + b
        n += 1
    return None


kb = fib(5)
# for i in range(6):
#     rst = next(kb)
#     print(rst)


for i in kb:
    print(i)


# 协程案例
def simple_coroutine():
    print('-> start')
    x = yield
    print('-> recived', x)


# 主线程
sc = simple_coroutine()

next(sc)
sc.send('zhe_xiao')
