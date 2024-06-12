import pytest
from selene import browser, have


@pytest.fixture
def browser_size(browser_driver):
    browser.driver.set_window_size(1920, 1080)


def test_search_goggle(browser_size):
    browser.open('https://google.com')
    browser.element('[name=q]').type('yashaka/selene').press_enter()
    browser.element('#search').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_no_search_goggle(browser_size):
    browser.open('https://google.com')
    browser.element('[name=q]').type('2353564tut6u77i').press_enter()
    browser.element('#botstuff').should(have.text('ничего не найдено.'))
