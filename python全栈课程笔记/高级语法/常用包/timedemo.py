# time模块 时间戳
# 从1970 1月1日 00:00:00 开始的秒数
# UTC 时间
# 夏令时
# 时间元组

import time

print(time.timezone)  # 时区
print(time.altzone)  # 夏令时

print(time.time())  # 时间戳

print(time.localtime())  # 时间结构

t = time.localtime()
tt = time.asctime(t)  # 返回格式化之后的时间
print(tt)

print(time.ctime())

ts = time.mktime(t)
print(ts)
print(type(ts))

for i in range(1, 10):
    # time.sleep(1)
    print('i=', i)


def func():
    time.sleep(2)


t0 = time.perf_counter()  # 包含cpu sleep 时间  ,process_time 不包含cpu时间
func()
t1 = time.perf_counter()
print(t1-t0)

mt = time.localtime()
print(time.strftime('%Y-%m-%d %H:%M', mt))
