def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)


a = [1, 5, 2, 1, 9, 1, 5, 10]
print(list(dedupe(a)))

print('------------------------------------')


def dedupe_1(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        print(val)
        # [exp1 if condition else exp2 for x in data]
        # 此处if...else主要起赋值作用，当data中的数据满足if条件时将其做exp1处理，否则按照exp2处理，最后统一生成为一个
        # 数据列表
        if val not in seen:
            yield item
            seen.add(val)


a = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3}, {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
print(list(dedupe_1(a, key=lambda d: (d['x'], d['y']))))
print(list(dedupe_1(a, key=lambda d: (d['x']))))

items = [0, 1, 2, 3, 4, 5, 6]
a = slice(2, 4)
print(items[2:4])
print(items[a])

items[a] = [10, 11]
print(items)

del items[a]

a = slice(5, 50, 2)
print(a.start)

print(a.stop)

print(a.step)

s = 'HelloWorld'
a.indices(len(s))

for i in range(*a.indices(len(s))):
    print(s[i])

