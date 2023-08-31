import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service()
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)



import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser: chrome or firefox")
    parser.addoption("--url", action="store", default="https://staging-cu.reposenergy.com/login", help="URL to test")

@pytest.fixture(scope="class")
def newset(request):
    browser_name = request.config.getoption("--browser")
    url = request.config.getoption("--url")

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")

    driver.get(url)
    request.cls.driver = driver
    yield driver
    driver.quit()


