
# def list_bianli():
#     alist=['小老弟','你在','干啥呢']
#     for i in alist:
#         print("这一步是啥意思?")
#         print(i)
def if_demo1():
    a=False
    if a:
        print('错的')
    else:
        print('对的')
def if_demo():
    a = 10
    b = 20
    if a > b:
        print('正确')
    else:
        print('错误')

x=1
y=10
def suanshubijaio_demo(x,y):
    a=0
    if x>y:
        for i in range(y+1,x):
            if i%2==0:
                a=a+i
        print(a)
    else:
        for i in range(x+1,y):
            if i%2==0:
                a=a+i
        print(a)


if __name__ == '__main__':
    # for i in range(5):
    #     print('hello world')
    #     for j in range(2):
    #             print('250')
    # for i in range(1,10):
    #     for j in range(1,i+1):
    #         print('%sx%s=%s'%(i,j,i*j),end=' ')
    #     print('')
    # nub=0
    # for i in range(1,51):
    #     if i%2 !=0:
    #         nub=nub+i
    # print(nub)
    # a=0
    # for i in range(1,10):
    #     for j in range(2,i+2):
    #         print('%sx%s=%s'%(i,j,i*j),end=' ')
    #         a=a+i
    # print(a)
    # a=0
    # for i in range(2,10,2):
    #     if i%2==0:
    #         a = a + i
    # print(a)
    # suanshubijaio_demo(x, y)
    a = 0
    while a < 20:
        print(a)
        a += 1

    # if_demo()
    # if_demo1()




