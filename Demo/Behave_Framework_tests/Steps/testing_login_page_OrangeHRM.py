import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Open OrangeHRM browser')
def open_orangeHRM_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://opensource-demo.orangehrmlive.com')
    time.sleep(2)


@when('Provide valid username and password')
def providing_valid_username_and_password(context):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)


@then('Verify login is successful or not')
def verify_login_page_title(context):
    assert context.driver.title == 'OrangeHRM'

