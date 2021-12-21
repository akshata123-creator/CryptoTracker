from selenium.webdriver.common.by import By


class LT_Locator(object):
    lt_email = "//input[@id='email']"
    lt_password = "//input[@id='pass']"
    lt_button = "//input[@value='login']"

    register_name = "//input[@id='name']"
    register_uname = "//input[@id='uname']"
    register_email = "//input[@id='email1']"
    register_num = "//input[@id='num']"
    register_password = "//input[@id='pass1']"
    register_button = "//input[@value='Sumbit']"

    search_box = "//input[@id='myInput']"
    search_crypto_ada = "//*[@id='myUL']/li[3]/a"
    search_crypto_algo = "//*[@id='myUL']/li[7]/a"
    search_crypto_1inch = "//*[@id='myUL']/li[1]/a"
    search_crypto_alice = "//*[@id='myUL']/li[8]/a"
    search_text = "//a[contains(text(),'Real Time Crypto Tracker')]"
    search_footer_text = "//div[@id='credit']"