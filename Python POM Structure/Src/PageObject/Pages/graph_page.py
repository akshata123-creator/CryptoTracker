import sys
from lib2to3.pgen2 import driver
sys.path.append(sys.path[0] + "/....")
from selenium.webdriver.common.by import By
from Src.PageObject.Locators import LT_Locator


class GT_Graph(object):
    def __init__(self, driver):
        self.driver = driver

        self.st_search_box = driver.find_element(By.XPATH, LT_Locator.search_box)
        self.st_search_crypto = driver.find_element(By.XPATH, LT_Locator.search_crypto)

    def get_ST_search(self):
        return self.st_search_box

    def get_ST_search_crypto(self):
        return self.st_search_crypto
