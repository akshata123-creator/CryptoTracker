import sys
import logging
# import os
sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())

import unittest
from time import sleep
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.register_page import RT_Register

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# information for registration
name = "ankitamodi"
uname = "ankitamodi"
register_email = "ankitamodi@gmail.com"
num = "7654321908"
register_password = "Ankitamodi@123"


class test_RT_RegisterPage(WebDriverSetup):
    logging.basicConfig(level=logging.DEBUG,
                        filename="C:/Users/akshata_chaudhari/PycharmProjects/Login_page/logging.txt",
                        format='Date-Time : %(asctime)s : Line No. : %(lineno)d - %(message)s')
    def test_Register_Page(self):

        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)

        self.driver.find_element(By.XPATH, "//label[@for='flip']").click()
        sleep(2)
        #driver.save_screenshot("C:/Users/akshata_chaudhari/PycharmProjects/Pom_structure/Screenshots/Register_Page.png")


        # Create an object of the Register Class
        rt_register_obj = RT_Register(driver)

        sleep(5)
        rt_register_obj.rt_register_name.send_keys(name)
        rt_register_obj.rt_register_uname.send_keys(uname)
        rt_register_obj.rt_register_email.send_keys(register_email)
        rt_register_obj.rt_register_num.send_keys(num)
        rt_register_obj.rt_register_password.send_keys(register_password)

        sleep(5)
        #driver.save_screenshot("C:/Users/akshata_chaudhari/PycharmProjects/Pom_structure/Screenshots/Register_Page_Info.png")

        rt_register_obj.rt_register_button.click()

        # See if the login is successful by checking the title, if successful than exit
        # else report an Error
        web_page_title = "Cryptotracker"

        try:
            if driver.title == web_page_title:
                print("\nUser signup successfully")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")

        sleep(2)

        #driver.save_screenshot("C:/Users/akshata_chaudhari/PycharmProjects/Pom_structure/Screenshots/After_Register.png")



        print("Register test completed successfully")

        if __name__ == '__main__':
            unittest.main()
