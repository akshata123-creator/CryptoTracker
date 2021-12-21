import datetime
import sys
sys.path.append(sys.path[0] + "/...")
import unittest
from time import sleep
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.register_page import RT_Register

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# information for registration
name = "akashshimpp"
uname = "akashshimpp"
register_email = "akashshimpp@gmail.com"
num = "7654321908"
register_password = "Akash@123"


class test_RT_RegisterPage(WebDriverSetup):
    def test_Register_Page(self):

        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)

        current_date_and_time = datetime.datetime.now()
        current_date_and_time_string = str(current_date_and_time.day) + "-" + str(current_date_and_time.month) + "-" + str(current_date_and_time.month) + "_" + str(current_date_and_time.strftime("%H")) + "-" + str(current_date_and_time.strftime("%M")) + "-" + str(current_date_and_time.strftime("%S"))

        self.driver.find_element(By.XPATH, "//label[@for='flip']").click()
        sleep(2)
        driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/Register_Page" + "_" + current_date_and_time_string + ".png")

        # Create an object of the Register Class
        rt_register_obj = RT_Register(driver)
        sleep(3)

        # TC1
    def test_verify_title(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)
        rt_register_obj = RT_Register(driver)

        assert rt_register_obj.rt_register_signup.text == "Signup"

    # TC2 - Verify if fields are editable
    def test_verify_editable(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)
        rt_register_obj = RT_Register(driver)

        element = rt_register_obj.rt_register_name
        assert element.is_enabled() is True
        element = rt_register_obj.rt_register_uname
        assert element.is_enabled() is True
        element = rt_register_obj.rt_register_email
        assert element.is_enabled() is True
        element = rt_register_obj.rt_register_num
        assert element.is_enabled() is True
        element = rt_register_obj.rt_register_password
        assert element.is_enabled() is True

    # TC3 - Verify is all fields are present or not
    def test_verify_fields_present(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)
        rt_register_obj = RT_Register(driver)

        elements = rt_register_obj.rt_register_name1
        assert len(elements) > 0
        elements = rt_register_obj.rt_register_uname1
        assert len(elements) > 0
        elements = rt_register_obj.rt_register_email1
        assert len(elements) > 0
        elements = rt_register_obj.rt_register_num1
        assert len(elements) > 0
        elements = rt_register_obj.rt_register_password1
        assert len(elements) > 0

        # TC4 - Verify all placeholders
    def test_verify_placeholders(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)
        rt_register_obj = RT_Register(driver)

        # name placeholder
        if "Enter your name" == rt_register_obj.rt_register_name.get_attribute("placeholder"):
            print("\nName Placeholder verified")
        else:
            print("\nName Placeholder not present")

        # username placeholder
        if "Enter your username" == rt_register_obj.rt_register_uname.get_attribute("placeholder"):
            print("\nUsername Placeholder verified")
        else:
            print("\nUsername Placeholder not present")

        # email placeholder
        if "Enter your email" == rt_register_obj.rt_register_email.get_attribute("placeholder"):
            print("\nEmail Placeholder verified")
        else:
            print("\nEmail Placeholder not present")

        # num placeholder
        if "Enter your 10 digit contact number" == rt_register_obj.rt_register_num.get_attribute("placeholder"):
            print("\nNum Placeholder verified")
        else:
            print("\nNum Placeholder not present")

        #  password placeholder
        if "Enter your password" == rt_register_obj.rt_register_password.get_attribute("placeholder"):
            print("\nPassword Placeholder verified")
        else:
            print("\nPassword Placeholder not present")

        # TC5 Verify submit btn
    def test_verify_submit_btn(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)
        rt_register_obj = RT_Register(driver)

        elements = rt_register_obj.rt_register_button1
        assert len(elements) > 0

    # TC6 Verify text
    def test_verify_text(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)
        rt_register_obj = RT_Register(driver)

        assert rt_register_obj.rt_register_text.text == "Already have an account? Login now"

    # TC7 Verify Login text
    def test_verify_login_text(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)
        rt_register_obj = RT_Register(driver)
        elements = rt_register_obj.rt_register_label

        assert len(elements) > 0

    # TC8 Verify bg img
    def test_verify_bg_img(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)
        rt_register_obj = RT_Register(driver)

        elements = rt_register_obj.rt_register_bg_img
        assert len(elements) > 0

    # TC9 Verify image text
    def test_verify_img_text(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)

        try:
            assert self.driver.find_element(By.XPATH,"//div/div").text == "Paper Money\\\\nIs Going\\\\nAway\\\\nComplete miles of journey\\\\nwith one step\\\\nLet\\\'s get started"
            if self.driver.find_element(By.XPATH,"//div/div").text:
                print("\n Img text verified")
        except Exception as error:
            print("\n Img text not verified")

    # TC10 Verify correct details
    def test_verify_correct_details(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)
        rt_register_obj = RT_Register(driver)

        rt_register_obj.rt_register_name.send_keys(name)
        rt_register_obj.rt_register_uname.send_keys(uname)
        rt_register_obj.rt_register_email.send_keys(register_email)
        rt_register_obj.rt_register_num.send_keys(num)
        rt_register_obj.rt_register_password.send_keys(register_password)

        sleep(5)
        current_date_and_time = datetime.datetime.now()
        current_date_and_time_string = str(current_date_and_time.day) + "-" + str(current_date_and_time.month) + "-" + str(current_date_and_time.month) + "_" + str(current_date_and_time.strftime("%H")) + "-" + str(current_date_and_time.strftime("%M")) + "-" + str(current_date_and_time.strftime("%S"))

        driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/Register_Page_Info" + "_" + current_date_and_time_string + ".png")
        rt_register_obj.rt_register_button.click()
        web_page_title = "Cryptotracker"

        try:
            if driver.title == web_page_title:
                print("\nUser signup successfully")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            print(error + "WebPage Failed to load")

        sleep(2)
        driver.save_screenshot("D:/PycharmProjects/Pom_structure/Screenshots/After_Register" + "_" + current_date_and_time_string + ".png")

        print("Register test completed successfully")

        if __name__ == '__main__':
            unittest.main()
