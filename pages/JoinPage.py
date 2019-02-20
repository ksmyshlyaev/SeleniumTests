from selenium.webdriver.common.action_chains import ActionChains
from Locators import Locator
from selenium.webdriver.common.by import By


class JoinPage(object):

    url = "https://github.com/join?source=login"

    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)

    def enter_username(self, username):
        self.actions.move_to_element(Locator.joinPage_username_id).click()
        self.driver.find_element(By.ID, Locator.joinPage_username_id).send_keys(username)

    def enter_email(self, email):
        self.actions.move_to_element(Locator.joinPage_email_id).click()
        self.driver.find_element(By.ID, Locator.joinPage_email_id).send_keys(email)

    def enter_password(self, password):
        self.actions.move_to_element(Locator.joinPage_password_id).click()
        self.driver.find_element(By.ID, Locator.joinPage_password_id).send_keys(password)

    def click_signUpButton(self):
        self.driver.find_element(By.ID, Locator.signUpButton_id).click()
