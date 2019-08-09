def simple_coroutine(a):
    print('-> start')
    b = yield a
    print('-> recived', a, b)
    c = yield a+b
    print('-> recived', a, b, c)


# 主线程
sc = simple_coroutine(5)

aa = next(sc)
print(aa)


bb = sc.send(6)
print(bb)

sc.send(7)
# cc = sc.send(7)

# print(type(cc))