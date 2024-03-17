import time

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By


@given('Open Orange_HRM browser')
def open_orangeHRM_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()
    context.driver.get('https://opensource-demo.orangehrmlive.com')
    time.sleep(2)


@when('providing valid UsernamE and PassworD')
def providing_valid_username_and_password(context):
    context.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)


@then('verifying login is successful or not')
def verify_login_page_title(context):
    assert context.driver.title == 'OrangeHRM'


@when('Passing the below {UserName} and {PassWord} in params')
def validating_username_and_password(context, UserName, PassWord):

    context.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(UserName)
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(PassWord)
    time.sleep(2)
    context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
    time.sleep(2)


@then('Verifying login Home status')
def verify_login_page_title(context):
    try:
        message = context.driver.find_element(By.XPATH,
                                              "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
    except:
        context.driver.close()
        assert False, "Test Fail"

    if message == "Dashboard":
        assert True


@when('Validating with below parameters')
def validating_username_and_password_with_query_params(context):

    for params in context.table:
        context.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys(params["userName"])
        time.sleep(2)
        context.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys(params["Password"])
        time.sleep(2)
        context.driver.find_element(By.XPATH, "//button[@type='submit']").click()
        time.sleep(2)


@then('Verifying login Home status is successful or not')
def verify_login_page_status(context):
    try:
        message = context.driver.find_element(By.XPATH,
                                              "//h6[@class='oxd-text oxd-text--h6 oxd-topbar-header-breadcrumb-module']").text
    except:
        context.driver.close()
        assert False, "Test Fail"

    if message == "Dashboard":
        assert True
