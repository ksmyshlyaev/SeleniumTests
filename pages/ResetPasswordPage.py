from Locators import Locator
from selenium.webdriver.common.by import By


class ResetPasswordPage(object):

    url = "https://github.com/password_reset"

    def __init__(self, driver):
        self.driver = driver

    def enter_email(self, email):
        self.driver.find_element(By.ID, Locator.email_id).clear()
        self.driver.find_element(By.ID, Locator.email_id).send_keys(email)

    def click_reset_button(self):
        self.driver.find_element(By.NAME, Locator.resetButton_name).click()
