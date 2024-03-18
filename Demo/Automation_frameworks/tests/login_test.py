import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestLogin():
    @pytest.fixture(scope="class")
    def test_setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.implicitly_wait(10)
        driver.maximize_window()
        yield
        driver.close()
        driver.quit()
        print('Test Completed')

    def test_login(self, test_setUp):
        driver.get("https://opensource-demo.orangehrmlive.com")
        driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        time.sleep(2)
        driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        time.sleep(2)
        driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)

    def test_logout(self, test_setUp):
        driver.find_element(By.CSS_SELECTOR, ".oxd-userdropdown-name").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//a[normalize-space()='Logout']").click()
        time.sleep(2)
