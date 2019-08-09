from collections import deque, defaultdict, Counter

q = deque(['a', 'b', 'c'])

print(q)
q.append('d')
print(q)

q.appendleft('x')
print(q)

d1 = {'one': 1, 'two': 2, 'three': 3}

print(d1['one'])
# print(d1['kk'])  # 崩溃, 用defaultdict 可以解决
print('-------------------------------')
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'

print(dd['key1'])
print(dd['key2'])

c = Counter('abcdefa')
print(c)
