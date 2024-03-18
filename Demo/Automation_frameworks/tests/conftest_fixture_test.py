import time

import pytest
from selenium import webdriver
from Demo.Automation_frameworks.pages.loginPage import LoginPage
from Demo.Automation_frameworks.pages.homePage import HomePage
from Demo.Automation_frameworks.utils import utils as utils


@pytest.mark.usefixtures("test_setup")
class TestLogin:

    def test_login(cls):
        driver = cls.driver
        driver.get(utils.URL)
        time.sleep(2)
        login = LoginPage(driver)
        login.enter_username(utils.USERNAME)
        time.sleep(2)
        login.enter_password(utils.PASSWORD)
        time.sleep(2)
        login.click_login_button()
        time.sleep(2)

    def test_logout(cls):
        driver = cls.driver
        homepage = HomePage(driver)
        homepage.click_on_dropdown()
        time.sleep(2)
        homepage.click_on_logout_button()
        time.sleep(2)
