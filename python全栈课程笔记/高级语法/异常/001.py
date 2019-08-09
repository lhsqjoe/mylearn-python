try:
    num = int(input('请输入数字:'))
    res = 100/num
    print('计算结果是：{}'.format(res))
except ZeroDivisionError as e:
    print(e)
    print("除数是0")
except NameError:
    print('name Error')

except AttributeError:
    print('AttributeError')
except Exception as e:  # 没必要，学习测试用
    print(e)
else:
    print("没错要执行")
finally:
    print("都要执行")

print('继续正常执行代码')



