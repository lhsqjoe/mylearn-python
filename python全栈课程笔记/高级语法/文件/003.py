import shelve

# 写
# shv = shelve.open(r'shv.db')
# shv['one'] = 1
# shv.close()

# 读文件
shv = shelve.open(r'shv.db')
try:
    print(shv['one'])
finally:
    shv.close()
