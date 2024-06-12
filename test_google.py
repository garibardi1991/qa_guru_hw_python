from selene import browser, have



def test_search_goggle():
    browser.open('https://google.com')
    browser.element('[name=q]').type('yashaka/selene').press_enter()
    browser.element('#search').should(have.text('Selene - User-oriented Web UI browser tests in Python'))

    browser.quit()


def test_no_search_goggle():
    browser.open('https://google.com')
    browser.element('[name=q]').type('2353564tut6u77i').press_enter()
    browser.element('#botstuff').should(have.text('ничего не найдено.'))

    browser.quit()

