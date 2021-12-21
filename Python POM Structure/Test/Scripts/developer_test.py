import sys

# import os
sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

import unittest
from time import sleep
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.developer_page import DT_Developer


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Add your username and password
email = "A@gmail.com"
password = "akshata"


class test_DT_Developer(WebDriverSetup):
    def test_Developer_Page(self):
        driver = self.driver
        driver.get("http://localhost/CryptoTracker/creator.html")

        sleep(3)
        # self.driver.find_element(By.XPATH, "//a[contains(text(),'Search')]").click()

        web_page_title = "Cryptotracker"

        try:
            if driver.title == web_page_title:
                print("\nuser is on Developer page")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")

        self.driver.save_screenshot(
            "C:/Users/akshata_chaudhari/PycharmProjects/Pom_structure/Screenshots/Developer_Page.png")

        text1 = "Developers &amp; Designers"
        text2 = driver.find_element(By.XPATH, "//h2[contains(.,'Developers & Designers')]").get_attribute("innerHTML")
        #driver.save_screenshot("C:/Users/akshata_chaudhari/PycharmProjects/Pom_structure/Screenshots/Home_Page.png")

        if text1 == text2:
            print("Pass")
            self.driver.close()
        else:
            print("Fail")
            self.driver.close()

        print("Developer test completed successfully")

        if __name__ == '__main__':
            unittest.main()