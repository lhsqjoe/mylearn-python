from datetime import datetime, timedelta

dt = datetime(2019, 8, 5)
print(dt.day)
print(dt.today())
print(dt.now())

t1 = datetime.now()
print(t1.strftime('%Y-%m-%d %H:%M:%S'))

td = timedelta(hours=1)  # 表示以小时的长度
print((t1+td).strftime('%Y-%m-%d %H:%M:%S'))