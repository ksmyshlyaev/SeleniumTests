from EnvironmentSetup import EnvironmentSetup
from pages.LoginPage import LoginPage
from selenium.webdriver.common.by import By
import unittest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import TimeoutException
import HtmlTestRunner
import os

scriptPath = os.path.abspath(__file__)
scriptDir = os.path.split(scriptPath)[0]
scriptDir = scriptDir[:-8]


class LoginTests(EnvironmentSetup):

    def test_WrongLogIn_1(self):

        driver = self.driver
        self.driver.get(LoginPage.url)
        login_page = LoginPage(driver)
        login_page.enter_username("testname")
        login_page.enter_password("testpassword")
        login_page.click_signInButton()
        try:
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.CLASS_NAME, "container")))
        except TimeoutException:
            self.fail('Element was not loaded in time')
        self.assertTrue("Incorrect username or password." in driver.page_source, "Error message is not displayed")

    def test_WrongLogIn_2(self):

        driver = self.driver
        self.driver.get(LoginPage.url)
        login_page = LoginPage(driver)
        login_page.enter_username("testname2")
        login_page.enter_password("testpassword2")
        login_page.click_signInButton()
        try:
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.CLASS_NAME, "container")))
        except TimeoutException:
            self.fail('Element was not loaded in time')
        self.assertTrue("Incorrect username or password." in driver.page_source, "Error message is not displayed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=scriptDir+'/reports'))
