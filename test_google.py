import pytest
from selene import browser, have


@pytest.fixture(autouse=True)
def browser_url():
    browser.config.base_url = 'https://google.com'


def test_search_goggle():
    browser.open('')
    browser.element('[name=q]').type('yashaka/selene').press_enter()
    browser.element('#search').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


def test_no_search_goggle():
    browser.open('')
    browser.element('[name=q]').type('2353564tut6u77i').press_enter()
    browser.element('#botstuff').should(have.text('По запросу 2353564tut6u77i ничего не найдено.'))
