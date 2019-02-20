from EnvironmentSetup import EnvironmentSetup
from pages.JoinPage import JoinPage
import unittest
import HtmlTestRunner
import os

scriptPath = os.path.abspath(__file__)
scriptDir = os.path.split(scriptPath)[0]
scriptDir = scriptDir[:-8]


class JoinTests(EnvironmentSetup):

    def test_WrongUsername(self):

        driver = self.driver
        self.driver.get(JoinPage.url)
        join_page = JoinPage(driver)
        join_page.enter_username("aaaaa")
        join_page.enter_email("dddddss@gmail.com")
        join_page.enter_password("aAa123!@#bBb321")
        join_page.click_signUpButton()
        self.assertTrue("There were problems creating your account." in driver.page_source, "Error message is not displayed")
        self.assertTrue("Login is already taken" in driver.page_source, "Error message is not displayed")

    def test_WrongEmail(self):

        driver = self.driver
        self.driver.get(JoinPage.url)
        join_page = JoinPage(driver)
        join_page.enter_username("dwdwdwdwdwdwww")
        join_page.enter_email("dsdsds@gmail.com")
        join_page.enter_password("aAa123!@#bBb321")
        join_page.click_signUpButton()
        self.assertTrue("There were problems creating your account." in driver.page_source, "Error message is not displayed")
        self.assertTrue("Email is invalid or already taken" in driver.page_source, "Error message is not displayed")

    def test_shortPassword(self):

        driver = self.driver
        self.driver.get(JoinPage.url)
        join_page = JoinPage(driver)
        join_page.enter_username("dwdwdwdwdwdwww")
        join_page.enter_email("dsdsssssds@gmail.com")
        join_page.enter_password("aaa")
        join_page.click_signUpButton()
        self.assertTrue("There were problems creating your account." in driver.page_source, "Error message is not displayed")
        self.assertTrue("Password is too short" in driver.page_source, "Error message is not displayed")

    def test_longPassword(self):

        driver = self.driver
        self.driver.get(JoinPage.url)
        join_page = JoinPage(driver)
        join_page.enter_username("dwdwdwdwdwdwww")
        join_page.enter_email("dsdsssssds@gmail.com")
        join_page.enter_password("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
        join_page.click_signUpButton()
        self.assertTrue("There were problems creating your account." in driver.page_source, "Error message is not displayed")
        self.assertTrue("Password is too long" in driver.page_source, "Error message is not displayed")

    def test_PasswordWithoutNumbers(self):

        driver = self.driver
        self.driver.get(JoinPage.url)
        join_page = JoinPage(driver)
        join_page.enter_username("dwdwdwdwdwdwww")
        join_page.enter_email("dsdsssssds@gmail.com")
        join_page.enter_password("aaaaaaaaaaaa")
        join_page.click_signUpButton()
        self.assertTrue("There were problems creating your account." in driver.page_source, "Error message is not displayed")
        self.assertTrue("Password needs at least 1 number" in driver.page_source, "Error message is not displayed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=scriptDir+'/reports'))
