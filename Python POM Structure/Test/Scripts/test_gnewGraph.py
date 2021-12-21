import pytesseract as tess
from pytesseract import pytesseract
import urllib.parse
import json
import requests
import datetime
import driver as driver
# from selenium import webdrive
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from Src.TestBase.WebDriverSetup import WebDriverSetup

tess.pytesseract.tesseract_cmd = r'D:\Graph Exe\tesseract.exe'
from PIL import Image

# run prog

class test_GT_NewGraphPage(WebDriverSetup):

    def test_NewGraph_Page(self):

        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)

        driver.get("https://crypto-tracker.swapnilg4u.repl.co/1inch")

        driver.find_element(By.XPATH, '//canvas[@id="canvas"]')

        driver.implicitly_wait(15)

        WebElement
        MouseHover = driver.find_element(By.ID, "canvas")

        current_date_and_time = datetime.datetime.now()
        current_date_and_time_string = str(current_date_and_time.day) + "-" + str(current_date_and_time.month) + "-" + str(
            current_date_and_time.month) + "_" + str(current_date_and_time.strftime("%H")) + "-" + str(
            current_date_and_time.strftime("%M")) + "-" + str(current_date_and_time.strftime("%S"))
        img = "screenshot" + "_" + current_date_and_time_string + ".png"
        driver.save_screenshot(img)
        #print(img)
        driver.implicitly_wait(45)
        driver.close()

        # values from graph
        graphExtractedInformation = pytesseract.image_to_string(Image.open(img))
        #print(img)

        start_index = graphExtractedInformation.find("Price in INR:")

        s = slice(start_index + 14, start_index + 21)

        # Get actual values of currency
        url = "https://x.wazirx.com/wazirx-falcon/api/v2.0/crypto_rates"#response = urllib.request.urlopen(url)
        jasondata = requests.get(url).json()

        # print statements
        print('Graph values:Price in INR: ' + graphExtractedInformation[s])
        print('Actual value:Price in INR: ' + jasondata['1inch']['inr'])

        GraphNum = float(graphExtractedInformation[s])
        JsonNum = float(jasondata['1inch']['inr'])

        if (JsonNum - 10) < GraphNum or (JsonNum + 10) > GraphNum:
            print('Pass')
        else:
            print('Fail')