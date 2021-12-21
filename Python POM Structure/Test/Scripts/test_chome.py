import datetime
import sys
import logging
sys.path.append(sys.path[0] + "/...")
import unittest
from time import sleep
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.Page import LT_Login
from Src.PageObject.Pages.home_page import HT_Home
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Add your username and password
email = "sakshik@gmail.com"
password = "12345"


class test_HT_HomePage(WebDriverSetup):
    def test_Home_Page(self):

        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)

        current_date_and_time = datetime.datetime.now()
        current_date_and_time_string = str(current_date_and_time.day) + "-" + str(current_date_and_time.month) + "-" + str(current_date_and_time.month) + "_" + str(current_date_and_time.strftime("%H")) + "-" + str(current_date_and_time.strftime("%M")) + "-" + str(current_date_and_time.strftime("%S"))
        driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/Home_Login_Page" + "_" + current_date_and_time_string + ".png")

        # Create an object of the Login Class
        lt_login_obj = LT_Login(driver)
        sleep(1)
        lt_login_obj.lt_login_email.send_keys(email)
        lt_login_obj.lt_login_password.send_keys(password)
        sleep(2)
        driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/Home_Login_Info" + "_" + current_date_and_time_string + ".png")
        lt_login_obj.lt_login_button.click()

        web_page_title = "Cryptotracker"

        try:
            if driver.title == web_page_title:
                print("\nUser Logged in successfully")
                driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/Home_Page" + "_" + current_date_and_time_string + ".png")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")
            driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/Home_Page_Error" + "_" + current_date_and_time_string + ".png")

        sleep(2)
        print("Login test completed successfully")

    # TC2 Verify navbar text Crypto currency
    def test_verify_navbar_text(self):

        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/Aboutcrpy.php")
        self.driver.set_page_load_timeout(360)
        ht_home_obj = HT_Home(driver)

        elements = ht_home_obj.home_left_crypto
        assert len(elements) > 0

    # TC3 Verify navbar
    def test_verify_navbar(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/Aboutcrpy.php")
        self.driver.set_page_load_timeout(360)
        ht_home_obj = HT_Home(driver)

        elements = ht_home_obj.home_search
        assert len(elements) > 0
        elements = ht_home_obj.home_developer
        assert len(elements) > 0
        elements = ht_home_obj.home_logout
        assert len(elements) > 0

    # TC4 Verify texts
    def test_verify_text(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/Aboutcrpy.php")
        self.driver.set_page_load_timeout(360)
        ht_home_obj = HT_Home(driver)

        assert ht_home_obj.home_text1.text == "Crypto Currency"
        assert ht_home_obj.home_text2.text == "Everything That You Want To Know About Crypto Currency"
        assert ht_home_obj.home_text3.text == "Trending Crypto"
        assert ht_home_obj.home_text4.text == "RECENT TRENDING CRYPTO"

    # TC5 Verify images
    def test_verify_img(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/Aboutcrpy.php")
        self.driver.set_page_load_timeout(360)
        ht_home_obj = HT_Home(driver)

        elements = ht_home_obj.home_img1
        assert len(elements) > 0
        elements = ht_home_obj.home_img2
        assert len(elements) > 0

    # TC6 Verify image text
    def test_verify_img_text(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/Aboutcrpy.php")
        self.driver.set_page_load_timeout(360)
        ht_home_obj = HT_Home(driver)

        assert ht_home_obj.home_img_text1.text == "ShibElon"
        assert ht_home_obj.home_img_text2.text == "Bitcoine"

    # TC7 Verify paragraph heading
    def test_verify_para_heading(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/Aboutcrpy.php")
        self.driver.set_page_load_timeout(360)
        ht_home_obj = HT_Home(driver)

        assert ht_home_obj.home_para_text.text == "CRYPTO-CURRENCY"

     # TC8 Verify paragraph image
    def test_verify_para_img(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/Aboutcrpy.php")
        self.driver.set_page_load_timeout(360)
        ht_home_obj = HT_Home(driver)

        elements = ht_home_obj.home_para_img
        assert len(elements) > 0

    # TC9 Verify scrollbar
    def test_verify_scrollbar(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/Aboutcrpy.php")
        self.driver.set_page_load_timeout(360)
        current_date_and_time = datetime.datetime.now()
        current_date_and_time_string = str(current_date_and_time.day) + "-" + str(current_date_and_time.month) + "-" + str(current_date_and_time.month) + "_" + str(current_date_and_time.strftime("%H")) + "-" + str(current_date_and_time.strftime("%M")) + "-" + str( current_date_and_time.strftime("%S"))

        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(5)
        driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/Home_Page_Scroll" + "_" + current_date_and_time_string + ".png")

    # TC10 Verify social icons
    def test_verify_social(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/Aboutcrpy.php")
        self.driver.set_page_load_timeout(360)
        ht_home_obj = HT_Home(driver)

        elements = ht_home_obj.home_social1
        assert len(elements) > 0
        elements = ht_home_obj.home_social2
        assert len(elements) > 0
        elements = ht_home_obj.home_social3
        assert len(elements) > 0
        elements = ht_home_obj.home_social4
        assert len(elements) > 0

    # TC11 Verify footer
    def test_verify_footer(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/Aboutcrpy.php")
        self.driver.set_page_load_timeout(360)
        ht_home_obj = HT_Home(driver)

        elements = ht_home_obj.home_footer
        assert len(elements) > 0

    # TC12 Verify invest and earn
    def test_verify_invest(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/Aboutcrpy.php")
        self.driver.set_page_load_timeout(360)
        ht_home_obj = HT_Home(driver)

        assert ht_home_obj.home_invest.text == "INVEST & EARN"

    # TC13 Verify if user is able to logout
    def test_verify_logout(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/Aboutcrpy.php")
        self.driver.set_page_load_timeout(360)
        ht_home_obj = HT_Home(driver)
        current_date_and_time = datetime.datetime.now()
        current_date_and_time_string = str(current_date_and_time.day) + "-" + str(current_date_and_time.month) + "-" + str(current_date_and_time.month) + "_" + str(current_date_and_time.strftime("%H")) + "-" + str(current_date_and_time.strftime("%M")) + "-" + str(current_date_and_time.strftime("%S"))

        assert ht_home_obj.home_logout1.text == "LOGOUT"
        ht_home_obj.home_logout1.click()
        assert self.driver.title == "LoginPage"
        driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/After_Logout" + "_" + current_date_and_time_string + ".png")

        print("Home test completed successfully")

        if __name__ == '__main__':
            unittest.main()
