import pytest
from selene import browser, have


@pytest.fixture(scope='session')
def browser_driver():
    browser.config.driver_name = 'firefox'
    yield
    browser.quit()
