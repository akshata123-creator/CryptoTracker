# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestTC12():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_tC12(self):
    self.driver.get("https://crypto-tracker.swapnilg4u.repl.co/")
    self.driver.set_window_size(1050, 660)
    assert self.driver.title == "Real Time Cryto Tracking"
    self.driver.find_element(By.ID, "myInput").click()
    element = self.driver.find_element(By.ID, "myInput")
    assert element.is_enabled() is True
    elements = self.driver.find_elements(By.ID, "myInput")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "myInput").send_keys("ada")
    self.driver.find_element(By.LINK_TEXT, "ADA").click()
    self.driver.close()
  
