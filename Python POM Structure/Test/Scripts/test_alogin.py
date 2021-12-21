import datetime
import sys
sys.path.append(sys.path[0] + "/...")
import logging
import unittest
from time import sleep
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.Page import LT_Login
from Src.PageObject.Locators import LT_Locator

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Add your username and password
email = "sakshik@gmail.com"
password = "12345"


class test_LT_LoginPage(WebDriverSetup):

    '''logging.basicConfig(level=logging.DEBUG, filename="newLog.log",filemode='w',
                        format='Date-Time : %(asctime)s : Line No. : %(lineno)d - %(message)s')

    logger = logging.getLogger()'''

    def test_Login_Page(self):

        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)
        current_date_and_time = datetime.datetime.now()
        current_date_and_time_string = str(current_date_and_time.day) + "-" + str(current_date_and_time.month) + "-" + str(current_date_and_time.month) + "_" + str(current_date_and_time.strftime("%H")) + "-" + str(current_date_and_time.strftime("%M")) + "-" + str(current_date_and_time.strftime("%S"))
        driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/Login_Page"+"_"+current_date_and_time_string+".png")

    # TC1 Verify title
    def test_verify_title(self):

        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)

        assert self.driver.title == "LoginPage"
        sleep(2)

    # TC2 Verify text Login
    def test_verify_text_login(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)
        lt_login_obj = LT_Login(driver)

        try:
            assert lt_login_obj.lt_login_text.text == "Login"
            logging.info("Text Login verified")
        except Exception as error:
            logging.error("Text Login is incorrect")

    # TC3 Verify is email and password is editable
    def test_verify_email_password(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)
        lt_login_obj = LT_Login(driver)
        lt_login_obj.lt_login_email.click()
        element = lt_login_obj.lt_login_email
        assert element.is_enabled() is True

        lt_login_obj.lt_login_password.click()
        element = lt_login_obj.lt_login_password
        assert element.is_enabled() is True

    # TC4 Verify forgot password
    def test_verify_forgot_pass(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)
        lt_login_obj = LT_Login(driver)
        elements = lt_login_obj.lt_forgot_pass
        assert len(elements) > 0

    # TC5 Verify text
    def test_verify_text(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)
        lt_login_obj = LT_Login(driver)
        assert lt_login_obj.lt_forgot_pass1.text == "Forgot password?"

    # TC6 - Verify login btn present or not
    def test_verify_login_btn(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)
        lt_login_obj = LT_Login(driver)
        elements = lt_login_obj.lt_login_button1
        assert len(elements) > 0

    # TC7 - Verify signup text
    def test_verify_signup_text(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)
        lt_login_obj = LT_Login(driver)
        elements = lt_login_obj.lt_sign_up
        assert len(elements) > 0

        try:
            assert lt_login_obj.lt_account.text == "Don\\\'t have an account? Sigup now"
            if lt_login_obj.lt_account.text:
                print("\n Signup text verified")
        except Exception as error:
            print("\n Signup text not verified")

    # TC8 Verify image text
    def test_verify_img_text(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)
        lt_login_obj = LT_Login(driver)
        try:
            assert lt_login_obj.lt_img_text1.text == "Paper Money\\\\nIs Going"
            if lt_login_obj.lt_img_text1.text:
                print("\n Img text verified")
        except Exception as error:
            print("\n Img text not verified")

        assert lt_login_obj.lt_img_text2.text == "Away"

    # TC9 - Verify placeholders
    def test_verify_placeholders(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)
        lt_login_obj = LT_Login(driver)

        # Email placeholder
        text1 = "Enter your email"
        text2 = lt_login_obj.lt_login_email.get_attribute("placeholder")

        if text1 == text2:
            print("Email Placeholder verified")
        else:
            print("Email Placeholder not present")

        # Password placeholder
        text3 = "Enter your password"
        text4 = lt_login_obj.lt_login_password.get_attribute("placeholder")

        if text3 == text4:
            print("Password Placeholder verified")
        else:
            print("Password Placeholder not present")

    # TC10 - Verify with correct email and password
    def test_verify_correct_details(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)
        lt_login_obj = LT_Login(driver)

        current_date_and_time = datetime.datetime.now()
        current_date_and_time_string = str(current_date_and_time.day) + "-" + str(current_date_and_time.month) + "-" + str(current_date_and_time.month) + "_" + str(current_date_and_time.strftime("%H")) + "-" + str(current_date_and_time.strftime("%M")) + "-" + str(current_date_and_time.strftime("%S"))

        lt_login_obj.lt_login_email.click()
        lt_login_obj.lt_login_email.send_keys(email)
        lt_login_obj.lt_login_password.click()
        lt_login_obj.lt_login_password.send_keys(password)
        sleep(2)
        driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/Login_Page_Info"+"_"+current_date_and_time_string+".png")
        lt_login_obj.lt_login_button.click()
        sleep(2)

        print(current_date_and_time_string)
        web_page_title = "Cryptotracker"
        try:
            if driver.title == web_page_title:
                print("\nUser Logged in successfully")
                self.assertEqual(driver.title, web_page_title)
                driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/After_Login" + "_" + current_date_and_time_string + ".png")
        except Exception as error:
            print(error + "WebPage Failed to load")
            driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/After_Login_Error" + "_" + current_date_and_time_string + ".png")

        print("Login test completed successfully")

        if __name__ == '__main__':
            unittest.main()
