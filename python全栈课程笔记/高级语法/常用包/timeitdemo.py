import timeit

c = '''
sum = []
for i in range(1000):
    sum.append(i)
'''
t1 = timeit.timeit(stmt=c, number=10000)
print(t1)
t2 = timeit.timeit(stmt='[i for i in range(1000)]', number=10000)
print(t2)
