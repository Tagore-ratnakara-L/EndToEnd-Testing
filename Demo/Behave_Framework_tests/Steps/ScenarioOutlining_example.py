import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Open OrangeHRM in browser')
def opening_OrangeHRM_in_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://opensource-demo.orangehrmlive.com')
    time.sleep(2)


@when('Validating {username} and {password}')
def validating_username_and_password(context, username, password):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(username)
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(password)
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)


@then('Verify login Home status')
def verify_login_page_title(context):
    try:
        message = context.driver.find_element(By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
    except:
        context.driver.close()
        assert False , "Test Fail"

    if message == "Dashboard":
        assert True

