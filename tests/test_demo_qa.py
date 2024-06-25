from selene import browser, have, be, by
import os


def test_automation_practice_form():
    browser.open('/automation-practice-form')
    browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))

    browser.element('#firstName').type('Igor')
    browser.element('#lastName').type('Trubikhov')
    browser.element('#userEmail').type('garibardi@mail.ru')

    browser.element('[for=gender-radio-1]').click()
    browser.element('[for=gender-radio-2]').click()
    browser.element('[for=gender-radio-3]').click()
    browser.element('[for=gender-radio-1]').click()

    browser.element('#userNumber').type('89523811047')

    browser.element('#dateOfBirthInput').click()
    browser.element('.react-datepicker__year-select').click().element('option[value="1991"]').click()
    browser.element('.react-datepicker__month-select').click().element('option[value="3"]').click()
    browser.element('.react-datepicker__day--025:not(.react-datepicker__day--outside-month)').click()

    browser.element('#subjectsInput').set_value('ma')
    browser.element(by.id('react-select-2-option-0')).should(have.text('Maths')).click()

    browser.element('[for="hobbies-checkbox-1"]').click()
    browser.element('[for="hobbies-checkbox-2"]').click()
    browser.element('[for="hobbies-checkbox-3"]').click()
    browser.element('[for="hobbies-checkbox-1"]').click()

    browser.element('#uploadPicture').send_keys(os.path.abspath('istockphoto-1443562748-612x612.jpg'))

    browser.element('#currentAddress-wrapper').element('.form-control').type('2-y Karavannay 15-4')

    browser.element('#state').click().element(by.id('react-select-3-option-2')).should(have.text('Haryana')).click()
    browser.element('#city').click().element(by.id('react-select-4-option-0')).should(have.text("Karnal")).click()

    browser.element('#submit').click()

    browser.element('.modal-header').should(have.text('Thanks for submitting the form'))
    browser.element('.table').all('td').even.should(have.exact_texts
                                                    ('Igor Trubikhov', 'garibardi@mail.ru', 'Male',
                                                     '8952381104', '25 April,1991', 'Maths',
                                                     'Reading, Music', 'istockphoto-1443562748-612x612.jpg', '2-y Karavannay 15-4',
                                                     'Haryana Karnal'))


