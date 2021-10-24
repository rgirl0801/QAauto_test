import pytest

from QAauto_test.constants import SESSION_COOKIE


@pytest.fixture(autouse=True)
def login(browser):
    browser.get('https://qastand.valhalla.pw/')
    browser.add_cookie(SESSION_COOKIE)
