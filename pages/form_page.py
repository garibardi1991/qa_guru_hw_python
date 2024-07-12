from pathlib import Path

from selene import browser, have, command


class RegistrationForm:
    def open(self):
        browser.open('/automation-practice-form/')
        browser.execute_script('document.querySelector(".body-height").style.transform = "scale(.75)"')
        browser.element('.practice-form-wrapper').should(have.text('Student Registration Form'))

    def type_first_name(self, value):
        browser.element('#firstName').type(value)

    def type_last_name(self, value):
        browser.element('#lastName').type(value)

    def type_email(self, email):
        browser.element('#userEmail').type(email)

    def type_birthday(self):
        browser.element('#dateOfBirthInput').click()
        browser.element('.react-datepicker__month-select').type('Aprile')
        browser.element('.react-datepicker__year-select').type('1991')
        browser.element(
            f'.react-datepicker__day--0{25}:not(.react-datepicker__day--outside-month)'
        ).click()

    def click_gender(self):
        browser.all('[name=gender]').element_by(have.value('Male')).element('..').click()

    def type_phone(self, phone):
        browser.element('#userNumber').type(phone)

    def type_subjects(self, subjects):
        browser.element('#subjectsInput').type(subjects).press_enter()

    def click_hobbies(self):
        browser.element('[for=hobbies-checkbox-2]').perform(command.js.scroll_into_view).click()

    def select_picture(self, file):
        browser.element('#uploadPicture').send_keys(str(Path(__file__).parent.parent.joinpath(
            f'resources/{file}')))

    def type_address(self, address):
        browser.element('#currentAddress').type(address)

    def type_state(self, state):
        browser.element('#state').click()
        browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(state)
        ).click()

    def type_city(self, city):
        browser.element('#city').click().element('#react-select-4-option-0').should(have.text(city)).click()

    def press_submit(self):
        browser.element('#submit').perform(command.js.click)

    def should_text(self, text):
        browser.element('[id=example-modal-sizes-title-lg]').should(
            have.text(text)
        )

    def should_exact_text(self, first_name, email, gender, phone, birthday, hobbies, hobbies2, photo, address, city):
        browser.element('.table').all('td').even.should(
            have.exact_texts(first_name, email, gender, phone,
                             birthday, hobbies, hobbies2, photo, address, city))


