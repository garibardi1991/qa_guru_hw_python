import pytest
from dotenv import load_dotenv

from utils import attach
from appium.options.android import UiAutomator2Options
from selene import browser
import os
from appium import webdriver


@pytest.fixture(scope = 'function', autouse = True)
def mobile_management():
    load_dotenv()
    login = os.getenv('USER_NAME')
    accesskey = os.getenv('ACCESS_KEY')
    options = UiAutomator2Options().load_capabilities({
        "platformName": "android",
        "platformVersion": "9.0",
        "deviceName": "Google Pixel 3",

        "app": "bs://sample.app",

        'bstack:options': {
            "projectName": "First Python project",
            "buildName": "browserstack-build-1",
            "sessionName": "BStack first_test",

            "userName": login,
            "accessKey": accesskey
        }
    })

    browser.config.driver = webdriver.Remote("http://hub.browserstack.com/wd/hub",
                                             options = options)

    browser.config.timeout = float(os.getenv('timeout', '10.0'))

    session_id = browser.driver.session_id

    yield

    attach.add_screenshot(browser)
    attach.add_xml(browser)
    session_id = browser.driver.session_id

    browser.quit()

    attach.add_video(session_id, login, accesskey)