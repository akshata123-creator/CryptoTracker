import sys

sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from Src.PageObject.Locators import LT_Locator


class HT_Home(object):
    def __init__(self, driver):
        self.driver = driver





    '''
        #self.ht_login_email = driver.find_element(By.XPATH, LT_Locator.lt_email)
        #self.lt_login_password = driver.find_element(By.XPATH, LT_Locator.lt_password)
        #self.lt_login_button = driver.find_element(By.XPATH, LT_Locator.lt_button)

    def get_LT_email(self):
        return self.lt_login_email

    def get_LT_password(self):
        return self.lt_login_password

    def get_LT_login_button(self):
        return self.lt_login_button
    '''