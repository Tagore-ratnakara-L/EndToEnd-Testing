import time

from selenium import webdriver
import HtmlTestRunner
import unittest
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from Demo.POM.Pages.LoginPage import LoginPage
from Demo.POM.Pages.HomePage import HomePage


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(Cls):
        Cls.driver = webdriver.Chrome()
        Cls.driver.maximize_window()

    def test_login_valid(self):
        driver = self.driver
        driver.get("https://opensource-demo.orangehrmlive.com")
        driver.implicitly_wait(10)

        login = LoginPage(driver)
        login.enter_username("Admin")
        time.sleep(2)
        login.enter_password("admin123")
        time.sleep(2)
        login.click_Login()
        time.sleep(2)
        homepage = HomePage(driver)
        time.sleep(2)
        homepage.Click_welcome()
        time.sleep(2)
        homepage.Click_logout()

    @classmethod
    def tearDownClass(Cls):
        print("tests completed successfully")
        Cls.driver.close()
        Cls.driver.quit()


if __name__ == '__main__':
    (unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner
    (output='C:\\Users\\Prasa\\PycharmProjects\\CompleteTestingEndToEnd\\Demo\\Reports')))
    unittest.main(verbosity=2)
