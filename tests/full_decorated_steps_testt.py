import allure
from allure_commons.types import Severity
from selene import browser, by


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Trubikhov")
@allure.feature("Автотест с Allure")
@allure.story("Просмотр issue у публичного репозитория github")
@allure.link("https://github.com", name="Testing")
def test_github_search_with_allure_steps():
    open_main_page()
    search_for_repository(repo="eroshenkoam/allure-example")
    go_to_repository(repo="eroshenkoam/allure-example")
    open_issue_tab()
    should_see_issue_with_name(name="с днем археолога!")


@allure.step('Открыть github.com')
def open_main_page():
    browser.open('/')


@allure.step("Ищем репозитория {repo}")
def search_for_repository(repo):
    browser.element("[data-target='qbsearch-input.inputButtonText']").click()
    browser.element("#query-builder-test").send_keys(repo).press_enter()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    browser.element("#issues-tab").click()


@allure.step("Проверяем наличие Issue с названием {name}")
def should_see_issue_with_name(name):
    browser.element(by.partial_text(name)).click()
