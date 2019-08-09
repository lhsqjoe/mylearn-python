try:
    print('Hello')
    raise ValueError
except ValueError as e:
    print('错了')