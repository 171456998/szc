from selenium import webdriver
from Common.Assert import Assertions
import time
import os
from Common.baseuii import baseUI
from Common import baseui
# from Common.baseuii import *


#打开浏览器
#
#确定chromedriver.exe的位置
class TestFirstUIDemo:
    def test_demo(self,driver):
        base = baseUI
        driver.get("http://192.168.60.132/#/login")

        # 输入用户名
        base.send_keys("输入用户名","//input[@name='username']","admin")
        # 输入密码
        base.send_keys("输入密码","//input[@name='password']","123456")
        # 点击登录
        base.click('点击登录',"//span[contains(text(),'登录')]")
        base.click('点击商品',"(//span[contains(text(),'商品')])[1]")
        base.click('点击添加商品',"(//span[contains(text(),'添加商品')])[1]")
        base.click('点击商品分类','(//span[@class="el-cascader__label"])[1]')
        base.click('点击手机数码',"//li[contains(text(),'手机数码')]")
        base.click('点击手机通讯',"//li[contains(text(),'手机通讯')]")
        base.send_keys('输入商品名称',"(//input [@type='text'])[2]",'szc')
        base.send_keys('输入副标题',"//label[contains(text(),'副标题')]/following-sibling::div//input", 'szcc')
        base.click('点击商品品牌',"//label[contains(text(),'商品品牌：')]/following-sibling::div//input")
        base.click('点击小米',"//span[contains(text(),'小米')]")
        base.click('点击下一步',"//span[contains(text(),'下一步，填写商品促销')]")
        base.click('点击特惠促销', "// span[contains(text(), '特惠促销')]")
        # 开始时间
        base.send_keys('输入时间',"//div[contains(text(),'开始时间')]//following-sibling::div//input","2019-04-03 00:00:00")

        # 结束时间
        base.send_keys('输入结束时间',"//div[contains(text(),'结束时间')]//following-sibling::div//input","2019-04-13 00:00:00")

        base.click('点击下一步',"//span[contains(text(),'下一步，填写商品属性')]")
        base.click('点击下一步',"//span[contains(text(),'下一步，选择商品关联')]")
        base.click('点击提交',"//span[contains(text(),'完成，提交商品')]")







