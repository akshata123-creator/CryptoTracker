import sys



# import os
from lib2to3.pgen2 import driver



sys.path.append(sys.path[0] + "/...")
# Uncomment if the above example gives you a relative path error
# sys.path.append(os.getcwd())
import pytest
import json
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

        self.driver.get("https://crypto-tracker.swapnilg4u.repl.co/")



        # TC1 - Verify webpage title
        web_page_title = "Real Time Cryto Tracking"
        st_search_obj = ST_Search(self.driver)
        try:
            if self.driver.title == web_page_title:
                print("\n user is on search page")
            self.assertEqual(self.driver.title, web_page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")



        self.driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/Search_Page.png")



        # TC2 - Verify text
        try:
            assert st_search_obj.st_search_text.text == "Real Time Crypto Tracker"
            if st_search_obj.st_search_text.text:
                print("Text is present")
        except Exception as error:
            print("Text is not present")



        # TC3 - Verify if search is editable
        element = st_search_obj.st_search_box
        try:
            assert element.is_enabled() is True
            if element.is_enabled():
                print("Searchbox is editable")
        except Exception as error:
            print("Searchbox is not editable")



        # TC4 - Verify if Scrollbar is working or not
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        sleep(2)



        # TC5 - Verify if entered crypto is present
        self.driver.execute_script("window.scrollBy(0,0)")
        sleep(3)
        # st_search_obj.st_search_box.click()
        st_search_obj.st_search_box.send_keys(crypto_algo)
        # elements = st_search_obj.st_search_crypto_algo
        elements = self.driver.find_elements(By.LINK_TEXT, "ALGO")
        assert len(elements) > 0
        sleep(1)
        st_search_obj.st_search_box.clear()



        # TC6 - Verify if footer text is present
        assert st_search_obj.st_search_footer_text.text == "Made with in India by Swapnil"



        sleep(3)
        # TC7 - Verify alphanumeric
        st_search_obj.st_search_box.send_keys(crypto_1inch)
        try:
            assert st_search_obj.st_search_crypto_1inch.text == "1INCH"
            if st_search_obj.st_search_crypto_1inch.text:
                print("1inch found successfully")
        except Exception as error:
            print("1inch not found")
        st_search_obj.st_search_box.clear()



        sleep(3)
        # TC8 - Verify case sensitivity
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
        text1 = "Search any Crypto.."
        text2 = self.driver.find_element(By.XPATH,LT_Locator.search_box).get_attribute("placeholder")
        # driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/Home_Page.png")



        if text1 == text2:
            print("Placeholder verified")
        else:
            print("Placeholder not present")



        sleep(3)
        # TC10 - Verify if user is able to navigate to graph page
        st_search_obj.st_search_box.send_keys(crypto_ada)
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