import pytest
from selene import browser, be

desktop_only = pytest.mark.parametrize("browser_management",
                                       [(1280, 720), (1920, 1080)], indirect=True,
                                       ids=['WEB_1280', 'WEB_1920'])
mobile_only = pytest.mark.parametrize("browser_management",
                                      [(414, 896)],
                                      indirect=True,
                                      ids=['Mobile_414'])


@mobile_only
def test_github_desktop(browser_management):
    if browser_management == 'mobile':
        pytest.skip(reason='Разрешение сторон экрана для телефона')

    browser.open('/')
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)


@desktop_only
def test_github_mobile(browser_management):
    if browser_management == 'desktop':
        pytest.skip(reason='Разрешение сторон экрана компьютера')

    browser.open('/')
    browser.element('.Button-label').click()
    browser.element('.HeaderMenu-link--sign-up').click()
    browser.element('#email').should(be.visible)
