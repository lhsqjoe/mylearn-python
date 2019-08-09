# 日历

import calendar

# 获取一年的日历

cal = calendar.calendar(2019)
print(cal)
# print(type(cal))
# w 日期列数
# l 周的行数
# c 月之间的间隔
cal = calendar.calendar(2019, l=0, c=5)
print(cal)

# 判读某年为闰年

print(calendar.isleap(2000))

# 获取指定年份之间闰年的个数
print(calendar.leapdays(2000, 2019))

print(calendar.month(2019, 8))

print(calendar.monthrange(2019, 8))  # 月从周几开始，天数

print(calendar.monthcalendar(2019, 8))  # 以矩阵的方式返回

calendar.prcal(2019)  # 打印一年的日历

calendar.prmonth(2019, 8)


print(calendar.weekday(2019, 8, 7))
