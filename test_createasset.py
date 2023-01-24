import driver as driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.wait import WebDriverWait
import pytest

#from .conftest import setup

@pytest.mark.usefixtures("setup")
class Test_Asset:

    def test_assetcreate(self):
        self.driver.find_element(By.NAME, "inputName").send_keys("4444444147")
        self.driver.find_element(By.NAME, "password").send_keys("repos1234")
        self.driver.find_element(By.XPATH,
                            "/html[1]/body[1]/div[1]/main[1]/div[1]/div[1]/div[1]/form[1]/button[1]/span[1]").click()
        time.sleep(5)
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, "//ul/li[3]").click()
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, "#place-order-btn").click()
        self.driver.find_element(By.XPATH, "//span[text()='200 L']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//input[@type='radio']").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//input[@type='checkbox']").click()
        time.sleep(4)
        self.driver.find_element(By.XPATH, "//span[text()='Place Order']").click()
        time.sleep(5)
        self.driver.find_element(By.XPATH, "//span[text()='Continue']").click()
        time.sleep(4)
        # driver.find_element(By.XPATH,"//span[text()='NEFT/RTGS']").click()
        time.sleep(10)

