import sys

# import os
sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

import unittest
from time import sleep
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.Page import LT_Login
from Src.PageObject.Pages.search_page import ST_Search


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Add your username and password
email = "sakshik@gmail.com"
password = "12345"
crypto = "ADA"


class test_GT_GraphPage(WebDriverSetup):

    def test_Graph_Page(self):

        driver = self.driver
        self.driver.get("https://crypto-tracker.swapnilg4u.repl.co/")
        self.driver.set_page_load_timeout(360)

        web_page_title = "Real Time Cryto Tracking"

        try:
            if self.driver.title == web_page_title:
                print("\nuser is on search page")
                self.assertEqual(self.driver.title, web_page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")

        self.driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/Search_Page.png")
        st_search_obj = ST_Search(self.driver)

        sleep(1)

        st_search_obj.st_search_box.send_keys(crypto)
        print("Crypto found successfully")
        self.driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/Search_Result.png")

        st_search_obj.st_search_crypto_ada.click()
        web_page_title = "Real Time ADA Tracker"

        try:
            if self.driver.title == web_page_title:
                print("\nuser is on graph page")
                self.assertEqual(self.driver.title, web_page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")

        #sleep(30)
        self.driver.save_screenshot(
            "D:/PycharmProjects/Pom_structure/Screenshots/Search_Result_Graph.png")

        print("Search test completed successfully")

        if __name__ == '__main__':
            unittest.main()
