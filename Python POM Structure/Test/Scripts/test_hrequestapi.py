import datetime
import sys
import logging

import self as self

sys.path.append(sys.path[0] + "/...")
import json
import requests
import unittest
from time import sleep
from Src.TestBase.WebDriverSetup import WebDriverSetup
from Src.PageObject.Pages.Page import LT_Login
from Src.PageObject.Pages.home_page import HT_Home
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC# Add your username and password
email = "sakshik@gmail.com"
password = "12345"
class test_RT_RequestPage(WebDriverSetup):
    def test_Request_Page(self):
        driver = self.driver
        self.driver.get("http://localhost/CryptoTracker/")
        self.driver.set_page_load_timeout(360)
        wazirx_api_domain = "https://api.wazirx.com"
        api_key = "1EpWVboqRoahRoihQZuqVDZlyQjhSeWW9zfVw9jPK66zaR0BHCHyD6R8QsIQhcTm"
        signature = "a0c4c94ce132d46cef99b1e585c2aa080c9a7d34e8ec6648a3b797e4a1fb1f84"
        Current_time = 1639548625774
        secrte_key = "HLDQlTr2NsD98yEBEud7EmLgFhhbzUeA8Idz6Tca" # tc 1 to check server code status
    def test1(self):
        pingValue = "https://api.wazirx.com/sapi/v1/ping"
        ping_value = requests.get(pingValue)
        print(ping_value) # tc2
    def test2(self):
        time = "https://api.wazirx.com/sapi/v1/time"
        time_value = requests.get(time).json()
        print(time_value) # tc3
    def test3(self):
        status = "https://api.wazirx.com/sapi/v1/systemStatus"
        system_status = requests.get(status).json()
        print(system_status) # tc4
    def test4(self):
        ticker = "https://api.wazirx.com/sapi/v1/ticker/24hr?symbol=btcinr"
        ticker_value = requests.get(ticker).json()
        print(ticker_value) # tc5
    def test5(self):
        orderbook = "https://api.wazirx.com/sapi/v1/depth?symbol=btcinr&limit=10"
        orderbook_value = requests.get(orderbook).json()
        print(orderbook_value) # tc6
    def test6(self):
        coin = "https://api.wazirx.com/sapi/v1/trades?symbol=btcinr&limit=10"
        coin_value = requests.get(coin).json()
        print(coin_value) # tc7
    def test7(self):
        post = "https://api.wazirx.com/sapi/v1/order/"
        source_code = {'id': 312089741,
        'isBuyerMaker': False,
        'price': '3720996.0',
        'qty': '0.00668',
        'quoteQty': '24856.25328',
        'time': 1639986231000}
        data = {'api_dev_key': "1EpWVboqRoahRoihQZuqVDZlyQjhSeWW9zfVw9jPK66zaR0BHCHyD6R8QsIQhcTm",
        'api_option': 'paste',
        'api_paste_code': source_code,
        'api_paste_format': 'python'}
        requests.post(post, data).json()
        print(requests.post(post,data).json())

