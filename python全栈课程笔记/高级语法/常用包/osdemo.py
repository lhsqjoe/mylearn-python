import os

print(os.getcwd())  # 获取当前工作目录
os.chdir('../')
print(os.getcwd())
print(os.listdir())
# os.mkdir('testa')
print(os.system('dir'))  # 执行shell 命令

print(os.getenv('PATH'))

print(os.curdir)
print(os.pardir)

print(os.sep)

print(os.linesep)  # 换行符

print(os.name)  # 操作系统名称
