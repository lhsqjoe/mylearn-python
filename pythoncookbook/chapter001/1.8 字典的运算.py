prices = {
    'ACME': 45.23,
    'AAPL': 612.78,
    'IBM': 205.55,
    'HPQ': 37.20,
    'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
print(min_price)

max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

prices_sorted = sorted(zip(prices.values(), prices.keys()))
print(prices_sorted)

print(min(prices.values()))
print(max(prices.values()))
print('---------------------------------')

print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))

prices = {'AAA': 45.23, 'ZZZ': 45.23}

print(min(zip(prices.values(), prices.keys())))
print(max(zip(prices.values(), prices.keys())))
