import time
import unittest
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import HtmlTestRunner


class MyTestCase(unittest.TestCase):
    """This setup class going to run all the requested tests in only one instance of browser"""

    @classmethod
    def setUpClass(Cls):
        Cls.driver = webdriver.Chrome()
        Cls.driver.implicitly_wait(10)
        Cls.driver.maximize_window()

    def test_search_1(self):
        self.driver.get("https://google.com")
        time.sleep(3)
        self.driver.find_element(By.NAME, "q").send_keys("Automation step by step")
        time.sleep(3)
        act = ActionChains(self.driver)
        (act.send_keys_to_element(self.driver.find_element(By.XPATH, "//textarea[@id='APjFqb']"))
         .send_keys(Keys.ENTER).perform())
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Automation step by step - Google Search")

    def test_search_2(self):
        self.driver.get("https://google.com")
        time.sleep(3)
        self.driver.find_element(By.NAME, "q").send_keys("Tagore ratnakar")
        time.sleep(3)
        act = ActionChains(self.driver)
        (act.send_keys_to_element(self.driver.find_element(By.XPATH, "//textarea[@id='APjFqb']"))
         .send_keys(Keys.ENTER).perform())
        x = self.driver.title
        print(x)
        self.assertEqual(x, "Tagore ratnakar - Google Search")

    @unittest.skip("This test is skipped test. ")
    def test_skip(self):
        """This test should be skipped."""
        pass

    @classmethod
    def tearDownClass(Cls):
        Cls.driver.close()
        Cls.driver.quit()



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:\\Users\\Prasa\\PycharmProjects\\CompleteTestingEndToEnd\\Demo\\Reports'))
    unittest.main(verbosity=2)
