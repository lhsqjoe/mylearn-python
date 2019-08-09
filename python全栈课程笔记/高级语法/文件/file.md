# 文件
 - 常用操作
    - 打开、关闭
    - 读写文件
    - 查找

# open 函数
 -  open(name[, mode[, buffering]])
    - mode
        - r
        - w
        - x 创建方式打开，文件已存在报错
        - a 追加模式
        - b 二进制模式
        - t 文本方式
        - '+' 可读写
 - with语句
 - seek
 - pickle 持久化  以文件的形式读写结构化数据 dump load 两个方法常用
 - shelve 持久化 类似字典 本质是个数据库