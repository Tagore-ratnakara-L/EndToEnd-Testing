from selenium.webdriver.common.by import By
from Demo.Automation_frameworks.Locators.locators import Locators


class HomePage(Locators):

    def __init__(self, driver):
        self.driver = driver

    def click_on_dropdown(self):
        self.driver.find_element(By.XPATH, self.Test_name_dropdown).click()

    def click_on_logout_button(self):
        self.driver.find_element(By.XPATH, self.logout_xpath).click()
