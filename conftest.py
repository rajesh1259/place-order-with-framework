import driver as driver
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support.wait import WebDriverWait




import pytest


@pytest.fixture(scope="class")
def setup(request):
    driver = webdriver.Chrome('../Customerapp/chromedriver')
    driver.implicitly_wait(10)
    driver.get("https://staging-cu.reposenergy.com/overview")
    request.cls.driver=driver
    yield
    driver.close()


