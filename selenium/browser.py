#coding=utf-8
import os
from selenium import webdriver

class CreateBrowserDriver():
    def create(browser_name):
        driverpath = os.getcwd() + os.sep  + 'driver'
        if browser_name == 'firefox':
            driverpath_firefox = driverpath + os.sep + 'geckodriver.exe'
            print(driverpath_firefox)
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
