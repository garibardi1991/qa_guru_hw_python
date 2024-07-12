import allure
from pages.form_page import RegistrationForm
from allure_commons.types import Severity


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "Trubikhov")
@allure.feature("Автотест с Allure DemoQA")
@allure.story("Тестирование формы регистрации DEMOQA")
@allure.link("https://demoqa.com/", name="Testing")
def test_student_registration_form():

    with allure.step("Открытие регистрационной формы"):
        registration_form = RegistrationForm()
        registration_form.open()

    with allure.step("Заполнение полей"):
        registration_form.type_first_name('Igor')
        registration_form.type_last_name('Trubikhov')
        registration_form.type_email('garibardi@mail.ru')
        registration_form.type_birthday()
        registration_form.click_gender()
        registration_form.type_phone('89523811047')
        registration_form.type_subjects('Maths')
        registration_form.click_hobbies()
        registration_form.select_picture('istockphoto-1443562748-612x612.jpg')
        registration_form.type_address('2-y Karavannay 15-4')
        registration_form.type_state('Haryana')
        registration_form.type_city("Karnal")
        registration_form.press_submit()

    with allure.step("Проверка результата"):
        registration_form.should_text('Thanks for submitting the form')
        registration_form.should_exact_text(
            'Igor Trubikhov',
            'garibardi@mail.ru',
            'Male',
            '8952381104',
            '25 April,1991',
            'Maths',
            'Reading',
            'istockphoto-1443562748-612x612.jpg',
            '2-y Karavannay 15-4',
            'Haryana Karnal'
        )
