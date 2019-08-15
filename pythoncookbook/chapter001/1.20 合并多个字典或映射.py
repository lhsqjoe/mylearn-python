a = {'x': 1, 'z': 3}
b = {'y': 2, 'z': 4}

from collections import ChainMap

c = ChainMap(a, b)
print(c['x'])
print(c['y'])
print(c['z'])

print(len(c))

print(list(c.keys()))

print(list(c.values()))

c['z'] = 10
c['w'] = 40
del c['x']

print(a)

# del c['y']  # 更新或删除操作总是影响的是列表中的第一个字典

values = ChainMap()
values['x'] = 1

values = values.new_child()
values['x'] = 2

values = values.new_child()
values['x'] = 3

print(values)

print(values['x'])
