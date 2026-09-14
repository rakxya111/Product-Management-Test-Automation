from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import pytest
import json

with open('config/config.json') as f:
    config = json.load(f)

def pytest_addoption(parser):
    parser.addoption(
        "--browser_name",
        action="store",
        default="chrome",
        help="Run tests on selected browser"
    )

@pytest.fixture(scope='function')
def driver(request):

    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        driver = webdriver.Chrome()

    elif browser_name == 'firefox':
        driver = webdriver.Firefox()

    else:
        raise ValueError(f"Unsupported browser : {browser_name}")

    driver.maximize_window()
    driver.get(config['url'])

    yield driver

    driver.quit()

@pytest.fixture(scope="function")
def wait(driver):
    return WebDriverWait(driver, config['timeout'])

