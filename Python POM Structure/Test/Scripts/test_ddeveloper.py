import datetime
import sys
sys.path.append(sys.path[0] + "/...")
import unittest
from time import sleep
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.developer_page import DT_Developer
from Src.PageObject.Pages.Page import LT_Login
from Src.PageObject.Pages.home_page import HT_Home
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Add your username and password
email = "sakshik@gmail.com"
password = "12345"


class test_DT_Developer(WebDriverSetup):
    def test_Developer_Page(self):
        driver = self.driver

        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)

        current_date_and_time = datetime.datetime.now()
        current_date_and_time_string = str(current_date_and_time.day) + "-" + str(current_date_and_time.month) + "-" + str(current_date_and_time.month) + "_" + str(current_date_and_time.strftime("%H")) + "-" + str(current_date_and_time.strftime("%M")) + "-" + str(current_date_and_time.strftime("%S"))

        # Create an object of the Login Class
        lt_login_obj = LT_Login(driver)

        sleep(1)

        lt_login_obj.lt_login_email.send_keys(email)
        lt_login_obj.lt_login_password.send_keys(password)

        sleep(1)
        driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/Dev_Login_Page" + "_" + current_date_and_time_string + ".png")
        lt_login_obj.lt_login_button.click()

        ht_home_obj = HT_Home(driver)
        driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/Dev_Home_Page" + "_" + current_date_and_time_string + ".png")
        sleep(2)
        ht_home_obj.home_developer1.click()


    # TC1 Verify title
    def test_verify_title(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/creator.html")
        self.driver.set_page_load_timeout(360)
        current_date_and_time = datetime.datetime.now()
        current_date_and_time_string = str(current_date_and_time.day) + "-" + str(current_date_and_time.month) + "-" + str(current_date_and_time.month) + "_" + str(current_date_and_time.strftime("%H")) + "-" + str(current_date_and_time.strftime("%M")) + "-" + str(current_date_and_time.strftime("%S"))

        assert self.driver.title == "Cryptotracker"
        driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/Dev_Page" + "_" + current_date_and_time_string + ".png")

    # TC2 Verify center text
    def test_verify_center_text(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/creator.html")
        self.driver.set_page_load_timeout(360)
        dt_dev_obj = DT_Developer(driver)

        text1 = "Developers &amp; Designers"
        text2 = dt_dev_obj.dev_text.get_attribute("innerHTML")

        if text1 == text2:
            print("Pass")
        else:
            print("Fail")

    # TC3 Verify navbar text present
    def test_verify_navbar_text(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/creator.html")
        self.driver.set_page_load_timeout(360)
        dt_dev_obj = DT_Developer(driver)

        elements = dt_dev_obj.dev_left_text
        assert len(elements) > 0

    # TC4 Verify navbar
    def test_verify_navbar(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/creator.html")
        self.driver.set_page_load_timeout(360)
        dt_dev_obj = DT_Developer(driver)
        elements = dt_dev_obj.dev_search

        assert len(elements) > 0
        elements = dt_dev_obj.dev_developer
        assert len(elements) > 0
        elements = dt_dev_obj.dev_logout
        assert len(elements) > 0

    # TC4 Verify developer img
    def test_verify_dev_img(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/creator.html")
        self.driver.set_page_load_timeout(360)
        dt_dev_obj = DT_Developer(driver)

        elements = dt_dev_obj.dev_img
        assert len(elements) > 0

    # TC5 Verify developer text
    def test_verify_dev_text(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/creator.html")
        self.driver.set_page_load_timeout(360)
        dt_dev_obj = DT_Developer(driver)
        assert dt_dev_obj.dev_img_text1.text == "Akash shimpi"
        assert dt_dev_obj.dev_img_text2.text == "Create, develop, play"

    # TC6 Verify scrollbar
    def test_verify_scrollbar(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/creator.html")
        self.driver.set_page_load_timeout(360)
        dt_dev_obj = DT_Developer(driver)
        current_date_and_time = datetime.datetime.now()
        current_date_and_time_string = str(current_date_and_time.day) + "-" + str(current_date_and_time.month) + "-" + str(current_date_and_time.month) + "_" + str(current_date_and_time.strftime("%H")) + "-" + str(current_date_and_time.strftime("%M")) + "-" + str(current_date_and_time.strftime("%S"))

        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(5)
        driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/Dev_Scroll" + "_" + current_date_and_time_string + ".png")

    # TC7 Verify social icon
    def test_verify_social(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/creator.html")
        self.driver.set_page_load_timeout(360)
        dt_dev_obj = DT_Developer(driver)

        elements = dt_dev_obj.dev_social
        assert len(elements) > 0

    # TC8 Verify Invest and Earn
    def test_verify_invest(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/creator.html")
        self.driver.set_page_load_timeout(360)
        dt_dev_obj = DT_Developer(driver)

        elements = dt_dev_obj.dev_invest
        assert len(elements) > 0

        # TC09 Verify bg img
    def test_verify_bg_img(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/creator.html")
        self.driver.set_page_load_timeout(360)
        dt_dev_obj = DT_Developer(driver)

        elements = dt_dev_obj.dev_bg_img
        assert len(elements) > 0

        print("Developer test completed successfully")

        if __name__ == '__main__':
            unittest.main()
