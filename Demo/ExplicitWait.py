from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()

driver.get("https://www.google.com")

driver.find_element(By.NAME, "q").send_keys("Automation")
# act = ActionChains(driver)
# (act.send_keys_to_element(driver.find_element(By.XPATH, "//textarea[@id='APjFqb']"))
#  .send_keys(Keys.ENTER).perform())
driver.find_element(By.XPATH, "//img[@alt='Google']").click()

wait = WebDriverWait(driver, 10)

try:
    element = wait.until(Ec.element_to_be_clickable((By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']")))
    print("Element is clickable")

except:
    print("Element is not clickable")
    exit()

element.click()
print("Test Completed")
driver.close()
driver.quit()
