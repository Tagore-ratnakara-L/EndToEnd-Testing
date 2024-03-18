from selenium.webdriver.common.by import By
from Demo.Automation_frameworks.Locators.locators import Locators


class LoginPage(Locators):

    def __init__(self, driver) -> None:
        self.driver = driver

    def enter_username(self, Username) -> None:
        # self.driver.find_element(By.XPATH, self.username_textbox).clear()
        self.driver.find_element(By.XPATH, self.Username_textbox_Xpath).send_keys(Username)

    def enter_password(self, Password) -> None:
        # self.driver.find_element(By.XPATH, self.password_textbox).clear()
        self.driver.find_element(By.XPATH, self.Password_textbox_Xpath).send_keys(Password)

    def click_login_button(self):
        self.driver.find_element(By.XPATH, self.Login_Btn_Xpath).click()
