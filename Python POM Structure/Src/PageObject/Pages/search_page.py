import sys
from lib2to3.pgen2 import driver



sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())



from selenium.webdriver.common.by import By
from Src.PageObject.Locators import LT_Locator




class ST_Search(object):
    def __init__(self, driver):
        self.driver = driver

        self.st_search_box = driver.find_element(By.XPATH, LT_Locator.search_box)
        self.st_search_crypto_ada = driver.find_element(By.XPATH, LT_Locator.search_crypto_ada)
        self.st_search_crypto_algo = driver.find_element(By.XPATH, LT_Locator.search_crypto_algo)
        self.st_search_crypto_1inch = driver.find_element(By.XPATH,LT_Locator.search_crypto_1inch)
        self.st_search_crypto_alice = driver.find_element(By.XPATH,LT_Locator.search_crypto_alice)
        self.st_search_text = driver.find_element(By.XPATH,LT_Locator.search_text)
        self.st_search_footer_text = driver.find_element(By.XPATH,LT_Locator.search_footer_text)



    def get_ST_search(self):
        return self.st_search_box



    def get_ST_search_crypto_ada(self):
        return self.st_search_crypto_ada



    def get_ST_search_crypto_algo(self):
        return self.st_search_crypto_algo



    def get_ST_search_crypto_1inch(self):
        return self.st_search_crypto_1inch



    def get_ST_search_crypto_alice(self):
        return self.st_search_crypto_alice



    def get_ST_search_text(self):
        return self.st_search_text



    def get_ST_search_footer_text(self):
        return self.st_search_footer_text