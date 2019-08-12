d = {
    'a': [1, 2, 3],
    'b': [4, 5]
}
e = {
    'a': {1, 2, 3},
    'b': {4, 5}
}

k = {2, 3, 5}
print(type(k))  # class set 集合


from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

print(d)

d = defaultdict(set)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)
print(d)

d = {}
d.setdefault('a', []).append(1)
d.setdefault('a', []).append(2)
d.setdefault('b', []).append(4)

print(d)

