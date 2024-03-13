from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
# Implicit waits
driver.implicitly_wait(10)

driver.get("https://www.google.com")

driver.find_element(By.NAME, "q").send_keys("Automation")
act = ActionChains(driver)
(act.send_keys_to_element(driver.find_element(By.XPATH, "//textarea[@id='APjFqb']"))
 .send_keys(Keys.ENTER).perform())

print("Test Completed")
driver.close()
driver.quit()
