from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.maximize_window()
driver.find_element(By.ID, "username").send_keys("rahulshettyacademy")
driver.find_element(By.ID, "password").send_keys("learning")
driver.find_element(By.XPATH, "//input[@id='signInBtn']").click()
time.sleep(5)
Card_titles = driver.find_elements(By.CSS_SELECTOR, ".card-title")
time.sleep(5)
name = ['iphone X', 'Blackberry']
n = 1
for i in Card_titles:
    if i.text in name:
        time.sleep(2)
        driver.find_element(By.XPATH, "(//*[@class='card-footer'])[" + str(n) + "]/button").click()
        n = n + 1
