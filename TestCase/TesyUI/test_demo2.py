from selenium import webdriver
from Common.Assert import Assertions
import time
import os
from Common.baseuii import baseUI
from Common import baseui
# from Common.baseuii import *

class TestFirstUIDemo:
    def test_demo(self,driver):
        base = baseUI(driver)
        # 打开网页
        driver.get("http://192.168.60.132/#/login")
        base.send_keys("输入用户名", "//input[@name='username']", "admin")
        base.send_keys("输入密码", "//input[@name='password']", "123456")
        # 点击登录
        base.click("点击登录","//span[contains(text(),'登录')]")

        # 点击营销
        base.click("点击营销", "(//span[contains(text(),'营销')])[1]")
        # 点击优惠券列表
        base.click("点击优惠券列表","(//span[contains(text(),'优惠券列表')])[1]")
        # 点击编辑编号为2的商品
        base.click("点击编辑", "(//span[contains(text(),'编辑')])[1]")
        # 点击优惠券类型
        base.click('点击优惠券类型',"(//label[contains(text(),'优惠券类型：')]/following-sibling::div//span)[1]")
        # 点击全场赠券
        base.click('点击全场赠券',"//span[contains(text(),'全场赠券')]")
        # 输入优惠券名称
        base.send_keys('输入优惠券名称',"//label[contains(text(),'优惠券名称：')]/following-sibling::div//input",'能看不能用')
        # 输入总发行量
        base.send_keys('输入总发行量',"//label[contains(text(),'总发行量：')]/following-sibling::div//input",'1')
        # 输入面额
        base.send_keys('输入面额',"//label[contains(text(),'面额：')]/following-sibling::div//input",'7')
        # 输入使用门槛
        base.send_keys('输入使用门槛',"//label[contains(text(),'使用门槛：')]/following-sibling::div//input","12")
        # 点击全场通用
        base.click('点击全场通用',"//label[contains(text(),'使用门槛：')]/following-sibling::div//input")
        # 点击提交
        base.click('点击提交',"//span[contains(text(),'提交')]")
        # 点击确定
        base.click('点击确定',"//span[contains(text(),'确定')]")
        # 添加断言
        # print(driver.page_source)打印,获取代码
        xpath = driver.find_element_by_xpath("//div[contains(@role,'alert')]/p")
        # print(xpath)  获取文字
        assertions = Assertions()
        assertions.assert_in_text(xpath.text,'修改成功')

