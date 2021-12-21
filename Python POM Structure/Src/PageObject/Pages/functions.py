import sys
from lib2to3.pgen2 import driver

sys.path.append(sys.path[0] + "/....")
from Src.TestBase.WebDriverSetup import WebDriverSetup


class Functions(object):
    def __init__(self, driver):
        self.driver = driver

    def sendKeys(self):
        return self.send_keys(self)

