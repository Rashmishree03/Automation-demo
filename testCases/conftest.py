from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
        print("---launching chrome browser----")
    elif browser == 'safari':
        driver = webdriver.Safari()
    else:
        driver = webdriver.Chrome()
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


#######################pytest html report ###########################
# it hooks for adding environment info to html report
# def pytest_configure(config):
#     config.metadata['Project Name'] = 'nop Commerce'
#     config.metadata['Module Name'] = 'customer'
#     config.metadata['Tester'] = 'Rashmi'


# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("Plugin", None)
