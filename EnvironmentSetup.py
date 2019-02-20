import unittest
import datetime
from selenium import webdriver
import os

scriptPath = os.path.abspath(__file__)
scriptDir = os.path.split(scriptPath)[0]


class EnvironmentSetup(unittest.TestCase):

    driver = None

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(executable_path=scriptDir+'/webdrivers/chromedriver.exe')
        print("Run started at :" + str(datetime.datetime.now()))
        print("Chrome environment Set Up" + "\n")
        cls.driver.maximize_window()

    @classmethod
    def tearDownClass(cls):
        if cls.driver is not None:
            print("Test Environment Destroyed")
            print("Run completed at: " + str(datetime.datetime.now()) + "\n")
            cls.driver.close()
            cls.driver.quit()
