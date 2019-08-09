with open(r'test.txt', 'r') as f:
    strline = f.readline()
    while strline:
        print(strline)
        strline = f.readline()

print('-------------------------')
with open(r'test.txt', 'r') as f:
    l = list(f)
    for line in l:
        print(line)

print('-------------------------')
with open(r'test.txt', 'r') as f:
    strChar = f.read()
    print(len(strChar))
    print(strChar)

print('*******************************************')

with open(r'test.txt', 'r') as f:
    f.seek(4, 0) # 第一个参数：  开始的偏移量  第二参数：表示要从哪个位置开始偏移；0代表从文件开头开始算起，1代表从当前位置开始算起，2代表从文件末尾算起。
    strChar = f.read()
    print(strChar)

print('-------------------------')
import time
with open(r'test.txt', 'r') as f:
    strChar = f.read(3)
    while strChar:
        time.sleep(1)
        print(strChar)
        strChar = f.read(3)

