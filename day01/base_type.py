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
