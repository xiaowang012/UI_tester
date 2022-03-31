#coding=utf-8
from time import sleep
from selenium import webdriver
import os
import keyboard

class CreateBrowserDriver():
    def create(browser_name):
        driverpath = os.getcwd() + os.sep  + 'driver'
        if browser_name == 'firefox':
            driverpath_firefox = driverpath + os.sep + 'geckodriver.exe'
            driver = webdriver.Firefox(executable_path = driverpath_firefox)
            return driver
        elif browser_name == 'chrome':
            driverpath_chrome = driverpath + os.sep + 'chromedriver.exe'
            driver = webdriver.Chrome(executable_path = driverpath_chrome)
            return driver
        elif browser_name == 'ie':
            driverpath_ie = driverpath + os.sep + 'IEDriverServer.exe'
            driver = webdriver.Ie(executable_path = driverpath_ie)
            return driver
        else:
            return False

class TestCase():
    #定义UI测试类
    def __init__(self,browser_type = None,url = None,find_ele_method = None,elemnet = None,input_data = None,confirm_button = None):
        self.driver = CreateBrowserDriver.create(browser_name = browser_type)
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        self.driver.get(url)
        if elemnet and input_data:
            self.driver.find_element_by_id(elemnet).send_keys(input_data)
            keyboard.press('TAB')
            self.driver.find_element_by_id('password').send_keys('123456')

        sleep(2)
        if confirm_button:
            self.driver.find_element_by_xpath(confirm_button).click()
        
        sleep(5)
        self.driver.quit()

    
    def func1(self):
        pass
    