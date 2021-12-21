import datetime
import sys
sys.path.append(sys.path[0] + "/...")
import pytest
import unittest
from time import sleep
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.Page import LT_Login
from Src.PageObject.Pages.search_page import ST_Search
from selenium.webdriver.common.by import By
from Src.PageObject.Locators import LT_Locator
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Add your username and password
email = "sakshik@gmail.com"
password = "12345"
crypto_ada = "ADA"
crypto_algo = "ALGO"
crypto_1inch = "1INCH"
crypto_alice = "alice"


class test_ST_SearchPage(WebDriverSetup):

    def test_Search_Page(self):

        driver = self.driver
        self.driver.get("https://crypto-tracker.swapnilg4u.repl.co/")
        self.driver.set_page_load_timeout(360)

        current_date_and_time = datetime.datetime.now()
        current_date_and_time_string = str(current_date_and_time.day) + "-" + str(current_date_and_time.month) + "-" + str(current_date_and_time.month) + "_" + str(current_date_and_time.strftime("%H")) + "-" + str(current_date_and_time.strftime("%M")) + "-" + str(current_date_and_time.strftime("%S"))
        driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/Search_Page" + "_" + current_date_and_time_string + ".png")

    # TC1 - Verify webpage title
    def test_verify_title(self):
        driver = self.driver
        self.driver.get("https://crypto-tracker.swapnilg4u.repl.co/")
        self.driver.set_page_load_timeout(360)

        web_page_title = "Real Time Cryto Tracking"
        try:
            if self.driver.title == web_page_title:
                print("\n user is on search page")
                self.assertEqual(self.driver.title, web_page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")

    # TC2 - Verify text
    def test_verify_text(self):

        driver = self.driver
        self.driver.get("https://crypto-tracker.swapnilg4u.repl.co/")
        self.driver.set_page_load_timeout(360)
        st_search_obj = ST_Search(self.driver)

        try:
            assert st_search_obj.st_search_text.text == "Real Time Crypto Tracker"
            if st_search_obj.st_search_text.text:
                print("Text is present")
        except Exception as error:
            print("Text is not present")

    # TC3 - Verify if search is editable
    def test_verify_editable(self):
        driver = self.driver
        self.driver.get("https://crypto-tracker.swapnilg4u.repl.co/")
        self.driver.set_page_load_timeout(360)
        st_search_obj = ST_Search(self.driver)
        current_date_and_time = datetime.datetime.now()
        current_date_and_time_string = str(current_date_and_time.day) + "-" + str(current_date_and_time.month) + "-" + str(current_date_and_time.month) + "_" + str(current_date_and_time.strftime("%H")) + "-" + str(current_date_and_time.strftime("%M")) + "-" + str(current_date_and_time.strftime("%S"))

        element = st_search_obj.st_search_box
        try:
            assert element.is_enabled() is True
            if element.is_enabled():
                print("Searchbox is editable")
        except Exception as error:
            print("Searchbox is not editable")

    # TC4 - Verify if Scrollbar is working or not
    def test_verify_scrollbar(self):
        driver = self.driver
        self.driver.get("https://crypto-tracker.swapnilg4u.repl.co/")
        self.driver.set_page_load_timeout(360)
        st_search_obj = ST_Search(self.driver)
        current_date_and_time = datetime.datetime.now()
        current_date_and_time_string = str(current_date_and_time.day) + "-" + str(current_date_and_time.month) + "-" + str(current_date_and_time.month) + "_" + str(current_date_and_time.strftime("%H")) + "-" + str(current_date_and_time.strftime("%M")) + "-" + str(current_date_and_time.strftime("%S"))

        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(2)
        driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/Search_Page_Scroll" + "_" + current_date_and_time_string + ".png")

    # TC5 - Verify if entered crypto is present
    def test_verify_crypto(self):
        driver = self.driver
        self.driver.get("https://crypto-tracker.swapnilg4u.repl.co/")
        self.driver.set_page_load_timeout(360)
        st_search_obj = ST_Search(self.driver)

        self.driver.execute_script("window.scrollBy(0,0)")
        sleep(3)
        st_search_obj.st_search_box.send_keys(crypto_algo)
        elements = st_search_obj.st_search_crypto_algo
        assert len(elements) > 0
        sleep(1)
        st_search_obj.st_search_box.clear()

    # TC6 - Verify if footer text is present
    def test_verify_footer(self):
        driver = self.driver
        self.driver.get("https://crypto-tracker.swapnilg4u.repl.co/")
        self.driver.set_page_load_timeout(360)
        st_search_obj = ST_Search(self.driver)

        assert st_search_obj.st_search_footer_text.text == "Made with in India by Swapnil"

        sleep(3)

    # TC7 - Verify alphanumeric
    def test_verify_alphanumeric(self):
        driver = self.driver
        self.driver.get("https://crypto-tracker.swapnilg4u.repl.co/")
        self.driver.set_page_load_timeout(360)
        st_search_obj = ST_Search(self.driver)

        st_search_obj.st_search_box.send_keys(crypto_1inch)
        sleep(3)
        try:
            assert st_search_obj.st_search_crypto_1inch.text == "1INCH"
            if st_search_obj.st_search_crypto_1inch.text:
                print("1inch found successfully")
        except Exception as error:
            print("1inch not found")
        st_search_obj.st_search_box.clear()

        sleep(3)

    # TC8 - Verify case sensitivity
    def test_verify_case_sensitivity(self):
        driver = self.driver
        self.driver.get("https://crypto-tracker.swapnilg4u.repl.co/")
        self.driver.set_page_load_timeout(360)
        st_search_obj = ST_Search(self.driver)

        st_search_obj.st_search_box.send_keys(crypto_alice)
        try:
            assert st_search_obj.st_search_crypto_alice.text == "ALICE"
            if st_search_obj.st_search_crypto_alice.text:
                print("Case sensitivity verified")
        except Exception as error:
            print("Case sensitivity not verified")
        st_search_obj.st_search_box.clear()
        sleep(3)

    # TC9 - Verify placeholders
    def test_verify_placeholders(self):
        driver = self.driver
        self.driver.get("https://crypto-tracker.swapnilg4u.repl.co/")
        self.driver.set_page_load_timeout(360)
        st_search_obj = ST_Search(self.driver)

        text1 = "Search any Crypto.."
        text2 = st_search_obj.st_search_box.get_attribute("placeholder")

        if text1 == text2:
            print("Placeholder verified")
        else:
            print("Placeholder not present")

        sleep(3)

    # TC10 - Verify if user is able to navigate to graph page
    def test_verify_navigate_graph(self):
        driver = self.driver
        self.driver.get("https://crypto-tracker.swapnilg4u.repl.co/")
        self.driver.set_page_load_timeout(360)
        st_search_obj = ST_Search(self.driver)
        current_date_and_time = datetime.datetime.now()
        current_date_and_time_string = str(current_date_and_time.day) + "-" + str(current_date_and_time.month) + "-" + str(current_date_and_time.month) + "_" + str(current_date_and_time.strftime("%H")) + "-" + str(current_date_and_time.strftime("%M")) + "-" + str(current_date_and_time.strftime("%S"))

        st_search_obj.st_search_box.send_keys(crypto_ada)
        sleep(2)
        driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/Search_Page_Result" + "_" + current_date_and_time_string + ".png")
        st_search_obj.st_search_crypto_ada.click()
        web_page_title = "Real Time ADA Tracker"

        try:
            if self.driver.title == web_page_title:
                print("\nuser is on graph page")
                self.assertEqual(self.driver.title, web_page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")

        #sleep(30)
        driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/Search_Result_Graph" + "_" + current_date_and_time_string + ".png")

        print("Search test completed successfully")

        if __name__ == '__main__':
            unittest.main()
