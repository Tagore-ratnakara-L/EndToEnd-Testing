from behave import *
from selenium import webdriver


@given('Opening browser')
def open_browser(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when('Provided google url in browser')
def providing_browser_url(context):
    context.driver.get('https://www.google.com')


@then('Verify title of the google page')
def verify_title(context):
    assert context.driver.title == 'Google'


