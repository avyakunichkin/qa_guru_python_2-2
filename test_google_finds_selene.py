import pytest
from selene.support.conditions import be
from selene.support.shared import browser
from selene import have


@pytest.fixture()
def setup_responsive_for_window():
    browser.config.window_width, browser.config.window_height = 1600, 900
    yield


def test_google_finds_selene_python(setup_responsive_for_window):
    browser.open('https://google.com/ncr')
    browser.element('[name=q]').type('selene python').press_enter()
    browser.element('[id=search]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))


def test_google_finds_selene_negative():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
