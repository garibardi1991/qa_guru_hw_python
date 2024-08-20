import allure
from allure_commons._allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


@allure.tag("mobile")
@allure.label("owner", "Igor Trubikhov")
@allure.feature("Википедия_примеры тесов для мобильных устройств")
@allure.story("Поиск на сайте")
def test_search_wikipedia():
    with step('Type search'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Verify content found'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


@allure.tag("mobile")
@allure.label("owner", "Igor Trubikhov")
@allure.feature("Википедия_примеры тесов для мобильных устройств")
@allure.story("Открытие результата поиска")
def test_open_search_result_wikipedia(mobile_management):
    with step('Type search'):
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/fragment_onboarding_skip_button")).click()
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('browserstack')
    with step('Open search result'):
        browser.all((AppiumBy.ID, "org.wikipedia.alpha:id/page_list_item_title")).first.click()
        browser.all((AppiumBy.XPATH, '//android.webkit.WebView[@text="BrowserStack"]')).should(be.present)