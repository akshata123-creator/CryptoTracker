import sys
import logging
# import os
sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

import unittest
from time import sleep
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.Page import LT_Login

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Add your username and password
email = "A@gmail.com"
password = "akshata"


class test_HT_HomePage(WebDriverSetup):

    def sendKeys(obj):
        return self.send_keys(self)

    def test_Home_Page(self):

        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)

        # Create an object of the Login Class
        lt_login_obj = LT_Login(driver)

        sleep(1)

        lt_login_obj.lt_login_email.send_keys(email)
        lt_login_obj.lt_login_password.send_keys(password)

        sleep(1)
        driver.save_screenshot("C:/Users/akshata_chaudhari/PycharmProjects/Pom_structure/Screenshots/Login_for_HomePage.png")

        # Click the login button to go to the dashboard
        lt_login_obj.lt_login_button.click()

        sleep(1)

        # See if the login is successful by checking the title, if successful than exit
        # else report an Error
        web_page_title = "Cryptotracker"

        try:
            if driver.title == web_page_title:
                print("\nUser Logged in successfully")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")

        sleep(2)
        print("Login test completed successfully")

        text1 = "Crypto Currency"
        text2 = self.driver.find_element(By.XPATH, "/html/body/header/nav/div/a").get_attribute("innerHTML")
        driver.save_screenshot("C:/Users/akshata_chaudhari/PycharmProjects/Pom_structure/Screenshots/Home_Page.png")


        if text1 == text2:
            print("Pass")
            self.driver.close()
        else:
            print("Fail")
            self.driver.close()

        print("we are on Home Page")


        if __name__ == '__main__':
            unittest.main()
