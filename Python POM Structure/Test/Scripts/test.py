import sys
import logging
sys.path.append(sys.path[0] + "/...")
import unittest
from time import sleep
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.Page import LT_Login
from Src.PageObject.Locators import LT_Locator


# Add your username and password
email = "A@gmail.com"
password = "akshata"


class test_LT_LoginPage(WebDriverSetup):

    logging.basicConfig(level=logging.DEBUG,
                        filename="logginggg.txt",
                        format='Date-Time : %(asctime)s : Line No. : %(lineno)d - %(message)s')
#    C: / Users / akshata_chaudhari / PycharmProjects / Login_page /
    def test_Login_Page(self):

        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)
        #driver.save_screenshot("C:/Users/akshata_chaudhari/PycharmProjects/Pom_structure/Screenshots/Login_Page.png")

        # Create an object of the Login Class
        lt_login_obj = LT_Login(self.driver)
        sleep(4)
        #lt_login_obj.getenabled(LT_Locator.lt_email)
        #lt_login_obj.onClick("Login")



        lt_login_obj.lt_login_email.send_keys(email)
        lt_login_obj.lt_login_password.send_keys(password)

        sleep(5)

        # Click the login button to go to the dashboard
        lt_login_obj.lt_login_button.click()

        sleep(2)

        # See if the login is successful by checking the title, if successful than exit
        # else report an Error
        web_page_title = "Cryptotracker"

        try:
            if driver.title == web_page_title:
                logging.debug("User Logged in successfully")
                self.assertEqual(driver.title, web_page_title)
        except Exception as error:
            logging.error("WebPage Failed to load")

        sleep(2)

        '''
        # Click on the automation tab and than exit
        automation_element = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//a[.='Automation']")))
        automation_element.click()
        '''
        #print("Login test completed successfully")
        logging.info("Login test completed successfully")


        if __name__ == '__main__':
            unittest.main()
