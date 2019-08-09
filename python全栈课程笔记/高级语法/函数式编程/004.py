l1 = [1, 2, 3, 4, 5]
l2 = sorted(l1, reverse=True)

print(l1)
print(l2)  # 逆序输出

l3 = [-1, 2, -3, -4, -1, -5]
l4 = sorted(l3, key=abs, reverse=True)
print(l4)

l5 = ['hello', 'Da',  'nm', 'kk']
print(sorted(l5, key=str.lower))


def myf2():
    def myf3():
        print('myf3')
        return 3
    return myf3


al = myf2()
print(type(al))
