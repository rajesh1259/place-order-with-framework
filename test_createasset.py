import time
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver import ChromeOptions

#from Customerapp.dataexcel import TestOpen

chrome_options = ChromeOptions()

@pytest.mark.usefixtures("newset")
class TestExample:

    def test_page(self,mytest):
        self.driver.implicitly_wait(15)
        #time.sleep(5)
        self.driver.find_element(By.ID, "mobile").send_keys("9823521834")
        #time.sleep(5)
        self.driver.find_element(By.ID, "Log In button").click()

        self.driver.find_element(By.ID, "Password").send_keys("repos1234")
        self.driver.find_element(By.ID, "Log In button").click()

        time.sleep(5)
        self.driver.refresh()



    # @pytest.fixture(params=TestOpen.test_myfun())
    # def mytest(self,request):
    #     return request.param



