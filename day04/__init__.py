def pingjie_demo():
    a=9
    b=10
    c=a+b
    print(c)
def pingjie1_demo():
    a='你是'
    b=250
    print(a,b)
def jiafa(a,b):
    a=1
    b=2
    a_b = a + b
    return a_b


if __name__ == '__main__':
    # pingjie_demo()
    # pingjie1_demo()
    # a = 1
    # b = 2
    # i = jiafa(a, b)
    # print(i)
    # list=[1,2,3,4,5,6,7,8,9]
    # list[4]=1
    # print(list)
    # print(list[1])
    # print(list[-2])
    # print(list.pop(-1))
    # print(list)
    # print(list.pop(-3))
    # print(list)
    # zidian={'name': 'ysl', 'pwd': '123456'}
    # print(zidian)
    # print(zidian['pwd'])
    # zidian.pop('pwd')
    # print(zidian)
    # for i in range(5):
    #     print('hello world ',end='   ')
    # print(' ')
    # alist='我,你,他,老王'
    # # for i in alist:
    # #     print(i)
    # for i in range(3):
    #       print((alist),end='')
    # print('')
    # astr='撒个谎发空间很宽松'#
    # assert  '我' not in astr
    # assert '我' in astr
    # a=0
    # while a<3:
    #     print('你是250')
    #     a+=1
    # try:
    #     assert '你' in astr
    # except:
    #     print('报错啦.响应断言没通过')
    # print('________')
    for i in range(5):
        print(i)
        if i ==3:
            continue
        print('第%s次循环至最后一行代码\n'%i)
    for i in range(5):
        print(i)
        if i ==3:
            break
        print('第%s次循环至最后一行代码\n'%i)



    pass

import requests