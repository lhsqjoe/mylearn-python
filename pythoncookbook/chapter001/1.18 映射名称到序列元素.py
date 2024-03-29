from collections import namedtuple

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber('jonesy@example.com', '2012-10-19')

print(sub)
print(sub.addr)
print(sub.joined)

print(len(sub))

addr, joined = sub

print(addr)
print(joined)

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)


def dict_to_stock(s):
    return stock_prototype._replace(**s)


a = {'name': 'ACME', 'shares': 100, 'price': 123.45}

print(dict_to_stock(a))

b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}

print(dict_to_stock(b))
