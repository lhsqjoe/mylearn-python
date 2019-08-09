import functools


def add(x, y):
    return x + y


print(functools.reduce(add, [1, 2, 3, 4, 5]))  # 相当于1+2+3+4+5


#  filter

def isEven(x):
    return x % 2 == 0


l2 = filter(isEven, [1, 2, 3, 4, 5, 6])

for i in l2:
    print(i)


# 闭包


def myF4(*args):
    def myF5():
        rst = 0
        for n in args:
            rst += n
        return rst

    return myF5


f5 = myF4(1, 2, 3, 4, 5)
print(f5())
