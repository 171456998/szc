# model 模块  main 主要的  print 打印 def  声明方法  int 整数  demo  例子

# def str_demo():
    # 声明aint变量,并赋值
    # aint = 1
    # print(aint)
    # # 打印aint的值
    # print(type(aint))


# def str_demo():
    # 声明aint变量,并赋值'1'(''代表该值得数据类型)
    # aint = '1'
    # print(aint)
    # print(type(aint))

def float_demo():
    afloat=1.91
    print(afloat)
    print(type(afloat))

def str_demo9():
    a='hello '
    b=250
    print('%s%s'%(a,b))

# 声明一个add方法 参数有两个 aint,bint
def add(aint, bint):
    #  打印aint参数
    print(aint)
    # 打印bint参数
    print(bint)
    # 返回 aint除以bint,return(返回)代表代码结束.
    return aint / bint


if __name__ == '__main__':
    str_demo9()
    # 提取变量 ctrl+alt+v
    # 调用add方法,传入值1,2,得到返回值,赋值给add1变量
    # add1 = add(1, 2)
    # print(add1)
    pass
def list_demo():
    alist = [4, 'ysl', '8', 7]
    print(alist)
    # 通过索引访问 元素
    print(alist[0])
    print(alist[1])
    # 倒序访问
    print(alist[-1])
    print(alist[-2])

# 更新列表中的元素
def list_update(alist):
    alist[0] = 1
    print(alist[0])
    print(alist)

# 切片操作
def list_update1(alist):
    # 从索引2 的位置 取 到索引5
    print(alist[2:6])
    # 从索引0 的位置 取 到索引5
    print(alist[:6])
    # 从索引3 的位置 取 到索引末尾.
    print(alist[3:])

# 列表/集合
if __name__ == '__main__':
    alist = [4, 'ysl', '8', 7,6,2,5]
    list_update1(alist)


# 这是一个注释
# model  模块
# main 主要的
# print 打印
# def 声明方法
# int 整数
# demo 例子
# return 返回
# 代码的层级关系 通过 缩进来表示
# class 类,类型
# str string 字符
# 合法标识符(变量名方法名) : 必须以字母或者_开头,剩下的可以是字母数字,下划线,大小写敏感, 不可用关键字做标识符
# ctrl+alt+L 格式化代码
# ctrl+K  commit 代码
# ctrl + shift + K  push 代码

# 声明一个int_demo 方法
def int_demo():
    # 声明aint变量 , 并赋值 1
    aint = 1
    # 打印 aint 的值
    print(aint)
    # 打印 aint 的 类型; type(aint): 获取aint的类型
    print(type(aint))


# 声明一个 str_demo 方法
def str_demo():
    # 声明astr变量 , 并赋值 '1'
    astr = '1'
    # 打印 astr 的值
    print(astr)
    # 打印 astr 的 类型; type(astr): 获取astr的类型
    print(type(astr))

    # 不写
    print('--------------')
    astr = 1
    # 打印 astr 的值
    print(astr)
    # 打印 astr 的 类型; type(astr): 获取astr的类型
    print(type(astr))

# 演示字符串拼接 : +
def str_demo1():
    a= 'hello'
    b= ' world'
    return a+b

# 字符串拼接: %s
def str_demo2():
    a= 'hello '
    b= 250
    # print(a+ str(b))
    print('a 是 : %s;b 是 : %s'%(a,b))

# 去掉两头空格
def str_demo3():
    astr = ' ysl '
    # astr 是变量 也叫 对象  ,对象 . 可以调用对象的方法
    print(astr)
    print(astr.strip())


# 12
# 声明一个add 方法 参数有两个 aint,bint
def add(aint, bint):
    # 打印aint参数
    print(aint)
    # 打印bint参数
    print(bint)
    # 返回 aint+bint
    return aint + bint

# 声明一个 float_demo 方法
def float_demo():
    # 声明afloat变量 , 并赋值 1.90
    afloat = 1.90
    # 打印 afloat 的值
    print(afloat)
    # 打印 afloat 的 类型; type(afloat): 获取afloat的类型
    print(type(afloat))

if __name__ == '__main__':
    str_demo3()
    # str_demo2()
    # print(str_demo1())
    # float_demo()
    # str_demo()
    # int_demo()
    # 提取变量  ctrl+alt+V
    # 调用add方法 传入1, 2,得到返回值 ,赋值给result变量
    # 指定参数传参
    # result = add(bint=2,aint=1)
    # print(result)
    # 默认参数传参
    # add(2,1)
    pass
