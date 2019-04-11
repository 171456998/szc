import os
# os指与目录相关
if __name__ == '__main__':

    # 获取当前目录路径
    # getcwd = os.getcwd()
    # print(getcwd)
    # 获取上级目录路径
    # abspath = os.path.abspath('..')
    # print(abspath)
    # 获取上上级目录路径
    # abspath1 = os.path.abspath('../..')
    # print(abspath1)
    pass
    # 绝对路径 C:\Users\Administrator\PycharmProjects\myedu
    # 相对路径 ../test.text
    # w+ 代表读写模式,写入时会覆盖原文档内容
    text_io = open('../test.text', 'w+')
    text_io.write("我呵呵呵")
    # a+ 代表读写模式,写入时不会覆盖 原文档内容,相当于追加内容
    text_io = open('../test.text', 'a+')
    text_io.write("我呵呵呵")
    # r 代表只读模式,不可写入
    text_io = open('../test.text', 'r')
    # 只读取第一行
    readline = text_io.readline()
    print(readline)
    # 读取所有行,并返回一个list对象
    readlines = text_io.readlines()
    print(readlines)
    pass






