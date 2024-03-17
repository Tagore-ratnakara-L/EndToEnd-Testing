import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Navigate to OrangeHRM in browser')
def navigating_OrangeHRM_in_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://opensource-demo.orangehrmlive.com')
    time.sleep(2)


@when('Validating with below params')
def validating_username_and_password_with_query_params(context):

    for params in context.table:
        context.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(params["userName"])
        time.sleep(2)
        context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(params["password"])
        time.sleep(2)
        context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)


@then('Verify login Home status is successful or not')
def verify_login_page_status(context):
    try:
        message = context.driver.find_element(By.XPATH, "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
    except:
        context.driver.close()
        assert False , "Test Fail"

    if message == "Dashboard":
        assert True

