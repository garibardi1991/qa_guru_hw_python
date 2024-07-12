import pytest
from selene import browser
from selenium import webdriver


@pytest.fixture(scope='session', autouse=True)
def browser_driver():
    # browser.config.driver_name = 'firefox'
    browser.config.base_url = 'https://demoqa.com'
    driver_options = webdriver.ChromeOptions()
    driver_options.add_argument('--headless=new')
    browser.config.driver_options = driver_options
    driver_options.page_load_strategy = 'eager'
    browser.config.window_height = 1200
    browser.config.window_width = 1920

    yield
    browser.quit()



