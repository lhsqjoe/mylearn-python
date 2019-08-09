l1 = [i for i in range(10)]
print(l1)


def mulTen(n):
    return n * 10


l2 = map(mulTen, l1)
print(type(l2))

for i in l2:
    print(i)

l3 = [i for i in l2]
print(l3)  # 看下结果


