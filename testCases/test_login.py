import os

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_01:
    print("hi")
    baseURL = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUsername()
    password = ReadConfig.getPassword()

    logger = LogGen.loggen()

    @pytest.mark.login
    def test_login(self, setup):
        self.logger.info("-----------Test_login01------------")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.lp = LoginPage(self.driver)
        self.lp.setusername(self.username)
        self.lp.setpassword(self.password)
        self.lp.clicklogin()
        act_title = self.driver.title
        if act_title == "OrangeHRM":
            assert True
            self.logger.info("Successfully logged in to Orange HRM")
        else:
            self.driver.save_screenshot(os.path.dirname(os.getcwd()) + "/Screenshots/" + "test_loginTitle.png")
            assert False
        self.driver.close()

    @pytest.mark.home
    def test_login2(self, setup):
        self.logger.info("-----------Test_login02------------")