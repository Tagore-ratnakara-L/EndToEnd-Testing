import pytest


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Type in browser name e.g.chrome OR firefox ")


def get_browser(request):
    return request.config.getoption("--browser")


@pytest.fixture(scope="class")
def test_setup(request):
    from selenium import webdriver
    browser = get_browser(request)
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'firefox':
        driver = webdriver.Firefox()
    request.cls.driver = driver
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield
    driver.close()
    driver.quit()
    print('Test Completed')
