
# class 类
# object  对象/或者所有类的父类
# 声明类的语法:class:就是声明一个类:Human:类的名字; ():括号里面填这个类的 父类
class  Human(object):
    # 类的初始化方法
    def __init__(self,name,age,sex):
        # 将入参的name赋值类  类本身的name
        # 类的属性
        self.name=name
        self.age=age
        self.sex=sex
    # 类里面方法必传 self
    def myInfo(self):
        print('我叫%s,我今年%s岁,%s'%(self.name,self.age,self.sex))

    def myInfostr(self):
        print('我叫%s,我今年%s岁,%s' % (self.name, self.age, self.sex))
class Tester(Human):
    def zhiXxingCeShi(self):
        # 调用了父类的属性
        print(self.name)
        print('我在执行测试,别打扰我')
        # 调用了父类的方法
        self.myInfo()

if __name__ == '__main__':
    # = 后面  调用了这个类   传入了初始化的参数 , 参数必须传入,而且需要传完整
    # = 前面是对象名
    # 对象是类的实例化
    # human = Human('ysl',25,'男')
    # print(type(human))
    # 对象可使用类中的方法
    # human.myInfo()
    # info_str = human.myInfostr()
    # print(info_str)
    human1=Tester('szc',25,'男')
    human1.zhiXxingCeShi()

