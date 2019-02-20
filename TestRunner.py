from scripts.LoginTests import LoginTests
from scripts.ResetPasswordTests import  ResetPasswordTests
from scripts.JoinTests import  JoinTests
import HtmlTestRunner
import unittest
import os

scriptPath = os.path.abspath(__file__)
scriptDir = os.path.split(scriptPath)[0]

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=scriptDir+'/reports'))
