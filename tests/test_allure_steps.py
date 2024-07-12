import allure
from selene import browser, by, be


def test_github_search_with_allure_steps():
    with allure.step('Открыть github.com'):
        browser.open("/")
    with allure.step('Находим репозиторий eroshenkoam/allure-example'):
        browser.element("[data-target='qbsearch-input.inputButtonText']").click()
        browser.element("#query-builder-test").send_keys("eroshenkoam/allure-example").press_enter()
    with allure.step("Переходим по ссылке репозитория"):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()
    with allure.step("Открываем таб Issues"):
        browser.element("#issues-tab").click()
    with allure.step("Проверяем наличие Issue с текстом 'с днем археолога!'"):
        browser.element(by.partial_text("с днем археолога!")).should(be.visible)
