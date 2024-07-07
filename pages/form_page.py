from pathlib import Path

from selene import browser, have, command

from test_data.user import User


class RegistrationForm:
    def open(self):
        browser.open('/automation-practice-form')
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
        browser.all('.custom-checkbox').element_by(have.exact_text('Reading')).click()

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

    def should_exact_text(self, user: User):
        browser.element('.table').all('td').even.should(have.exact_texts(
            f'{user.first_name} {user.last_name}',
            f'{user.email}',
            f'{user.gender}',
            f'{user.phone}',
            f'{user.birthday}',
            f'{user.subject}',
            f'{user.hobbies}',
            f'{user.file}',
            f'{user.address}',
            f'{user.state} {user.city}'))

    def register(self, user: User):
        self.type_first_name(user.first_name)
        self.type_last_name(user.last_name)
        self.type_email(user.email)
        self.click_gender()
        self.type_phone(user.phone)
        self.type_birthday()
        self.type_subjects(user.subject)
        self.click_hobbies()
        self.select_picture(user.file)
        self.type_address(user.address)
        self.type_state(user.state)
        self.type_city(user.city)
        self.press_submit()


