from Locators import Locator
from selenium.webdriver.common.by import By


class LoginPage(object):

    url = "https://github.com/login"

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.ID, Locator.loginPage_username_id).clear()
        self.driver.find_element(By.ID, Locator.loginPage_username_id).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.ID, Locator.loginPage_password_id).clear()
        self.driver.find_element(By.ID, Locator.loginPage_password_id).send_keys(password)

    def click_signInButton(self):
        self.driver.find_element(By.NAME, Locator.signInButton_name).click()
