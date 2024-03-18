import pytest


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    driver = webdriver.Chrome()
    request.cls.driver = driver
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print('Test Completed')
