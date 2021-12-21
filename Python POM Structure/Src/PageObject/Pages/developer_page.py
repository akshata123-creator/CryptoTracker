import sys
from lib2to3.pgen2 import driver

sys.path.append(sys.path[0] + "/....")
# import os
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

from selenium.webdriver.common.by import By
from Src.PageObject.Locators import LT_Locator


class DT_Developer(object):
    def __init__(self, driver):
        self.driver = driver