import HtmlTestRunner
from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class GoogleSearch(unittest.TestCase):

    @classmethod
    def setUpClass(Cls):
        Cls.driver = webdriver.Chrome()
        Cls.driver.implicitly_wait(10)
        Cls.driver.maximize_window()

    def test_search_automation(self):
        self.driver.get("https://google.com")
        self.driver.find_element(By.NAME, "q").send_keys("Automation")
        self.driver.find_element(By.XPATH, "//img[@alt='Google']").click()
        self.driver.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").click()
        print(self.driver.title)

    @classmethod
    def tearDownClass(Cls):
        Cls.driver.close()
        Cls.driver.quit()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:\\Users\\Prasa\\PycharmProjects\\CompleteTestingEndToEnd\\Demo\\Reports"), verbosity=2)
