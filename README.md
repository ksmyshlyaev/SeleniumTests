# SeleniumTests
Test project for UI tests using python + selenium + unittest + html-testRunner.
It is written according to Page Object Model pattern.
Each testclass is stored in a separate module which can be useful to keep one set of tests apart from another.
The whole test suite runs by executing TestRunner.py file.
If you want to run any testclass (e.g. LoginTests.py) separately, you have to change your directory to SeleniumTests folder and then execute the following command:
```
python -m scripts.LoginTests
```
