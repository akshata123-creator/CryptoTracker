
import sys

sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())
from selenium.webdriver.common.by import By
from Src.PageObject.Locators import LT_Locator


class RT_Register(object):
    def __init__(self, driver):
        self.driver = driver
        self.rt_register_name = driver.find_element(By.XPATH, LT_Locator.register_name)
        self.rt_register_uname = driver.find_element(By.XPATH, LT_Locator.register_uname)
        self.rt_register_email = driver.find_element(By.XPATH, LT_Locator.register_email)
        self.rt_register_num = driver.find_element(By.XPATH, LT_Locator.register_num)
        self.rt_register_password = driver.find_element(By.XPATH, LT_Locator.register_password)
        self.rt_register_button = driver.find_element(By.XPATH, LT_Locator.register_button)

    def get_RT_name(self):
        return self.rt_register_name

    def get_RT_uname(self):
        return self.rt_register_uname

    def get_RT_email(self):
        return self.rt_register_email

    def get_RT_num(self):
        return self.rt_register_num

    def get_RT_password(self):
        return self.rt_register_password

    def get_RT_register_button(self):
        return self.rt_register_button
