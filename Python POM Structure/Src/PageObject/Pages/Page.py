import sys
from jproperties import Properties
sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from Src.PageObject.Locators import LT_Locator


class LT_Login(object):

    '''global configs
    configs = Properties()
    with open('Config.properties', 'rb') as read_prop:
        configs.load(read_prop)
    '''

    def __init__(self, driver):


        self.driver = driver

        self.lt_login_email = driver.find_element(By.XPATH, LT_Locator.lt_email)
        self.lt_login_password = driver.find_element(By.XPATH, LT_Locator.lt_password)
        self.lt_login_button = driver.find_element(By.XPATH, LT_Locator.lt_button)

    def get_LT_email(self):
        return self.lt_login_email

    def get_LT_password(self):
        return self.lt_login_password

    def get_LT_login_button(self):
        return self.lt_login_button

    '''def getLoginPageTitle(self):
        self.driver.title == configs.get("LoginTitle")
    
    def getenabled(self,elementname):
        element = self.driver.find_element(By.ID, elementname)
        assert element.is_enabled() is True

    def onClick(self,elementname):
        self.driver.find_element(By.LINK_TEXT,elementname).click()
'''
