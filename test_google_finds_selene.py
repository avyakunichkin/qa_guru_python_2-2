from selene.support.shared import browser
from selene import have

browser.open('https://google.com/ncr')
browser.element('[name=q]').type('selene python').press_enter()
browser.element('[id=search]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))
