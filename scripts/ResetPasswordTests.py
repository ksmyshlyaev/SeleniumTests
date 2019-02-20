from EnvironmentSetup import EnvironmentSetup
from pages.ResetPasswordPage import ResetPasswordPage
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


class ResetPasswordTests(EnvironmentSetup):

    def test_WrongEmail(self):

        driver = self.driver
        self.driver.get(ResetPasswordPage.url)
        reset_password_page = ResetPasswordPage(driver)
        reset_password_page.enter_email("fakeemail")
        reset_password_page.click_reset_button()
        try:
            WebDriverWait(driver, 10).until(
                ec.presence_of_element_located((By.CLASS_NAME, "container")))
        except TimeoutException:
            self.fail('Element was not loaded in time')
        self.assertTrue("Can't find that email, sorry." in driver.page_source, "Error message is not displayed")


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=scriptDir+'/reports'))

