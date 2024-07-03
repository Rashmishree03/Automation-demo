from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_name = "//input[@name='username']"
    textbox_password_name = "//input[@name='password']"
    button_login_xpath = "//button[@type='submit']"

    def __init__(self, driver):
        self.driver = driver

    def setusername(self, username):
        self.driver.find_element(By.XPATH, self.textbox_username_name).clear()
        self.driver.find_element(By.XPATH, self.textbox_username_name).send_keys(username)

    def setpassword(self, password):
        self.driver.find_element(By.XPATH, self.textbox_password_name).clear()
        self.driver.find_element(By.XPATH, self.textbox_password_name).send_keys(password)

    def clicklogin(self):
        self.driver.find_element(By.XPATH, self.button_login_xpath).click()
