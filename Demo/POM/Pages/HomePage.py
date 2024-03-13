from Demo.POM.Locators.Locators import LocatorsTest

from selenium.webdriver.common.by import By


class HomePage():

    def __init__(self, driver):
        self.driver = driver

    def Click_welcome(self):
        self.driver.find_element(By.CSS_SELECTOR, LocatorsTest.welcome_css_selector).click()

    def Click_logout(self):
        self.driver.find_element(By.XPATH, LocatorsTest.logout_xpath).click()
