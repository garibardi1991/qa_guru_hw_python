from test_data.user import User
from pages.form_page import RegistrationForm


def test_student_registration_form():
    form_page = RegistrationForm()
    man = User(first_name='Igor',
               last_name='Trubikhov',
               email='garibardi@mail.ru',
               gender='Male',
               phone='8952381104',
               birthday='25 April,1991',
               subject='Maths',
               file='istockphoto-1443562748-612x612.jpg',
               hobbies='Reading',
               address='2-y Karavannay 15-4',
               state='Haryana',
               city='Karnal')
    form_page.open()
    form_page.register(man)
    form_page.should_exact_text(man)
