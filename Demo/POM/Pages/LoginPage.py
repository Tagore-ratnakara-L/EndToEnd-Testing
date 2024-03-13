from selenium.webdriver.common.by import By
from Demo.POM.Locators.Locators import LocatorsTest


class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element(By.XPATH, LocatorsTest.Username_textbox_Xpath).clear()
        self.driver.find_element(By.XPATH, LocatorsTest.Username_textbox_Xpath).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, LocatorsTest.Password_textbox_Xpath).clear()
        self.driver.find_element(By.XPATH, LocatorsTest.Password_textbox_Xpath).send_keys(password)

    def click_Login(self):
        self.driver.find_element(By.XPATH, LocatorsTest.Login_Btn_Xpath).click()
