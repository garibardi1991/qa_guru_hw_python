import pytest
from selene import browser, be

desktop_only = pytest.mark.parametrize("browser_management_desktop",
                                       [(1280, 720), (1920, 1080)],
                                       ids=['WEB_1280', 'WEB_1920'])
mobile_only = pytest.mark.parametrize("browser_management_mobile",
                                      [(414, 896)],
                                      ids=['Mobile_414'])


@desktop_only
def test_github_desktop(browser_management_desktop):
    browser.open('/')
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)


@mobile_only
def test_github_mobile(browser_management_mobile):
    browser.open('/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)
