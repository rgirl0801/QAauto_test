import pytest

from constants import Links, POSITIVE_LOGIN_CREDENTIALS, NEGATIVE_LOGIN_CREDENTIALS
from functions import wait_for_url_to_be, login_ui


@pytest.mark.auth
class TestAuthorizationClass:

    @pytest.mark.smoke
    def test_login_positive(self, browser):
        browser.get(Links.login)  # step1
        browser.maximize_window()
        login_ui(browser, POSITIVE_LOGIN_CREDENTIALS['email'], POSITIVE_LOGIN_CREDENTIALS['password'])
        wait_for_url_to_be(browser, Links.profile)  # step5
        assert browser.get_cookie("session"), 'Отсуствует куки session'  # step6

    @pytest.mark.parametrize("email, password",
                             NEGATIVE_LOGIN_CREDENTIALS, ids=["empty email", "empty password", "invalid email",
                                                              "unregistered user"])
    @pytest.mark.search
    def test_login_negative(self, email, password, browser):
        browser.get(Links.login)  # step1
        browser.maximize_window()
        login_ui(browser, email, password)  # step2
        assert wait_for_url_to_be(browser, Links.login), 'Произошла авторизация'  # step4
