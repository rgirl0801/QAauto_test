import allure
import pytest

from constants import Links, POSITIVE_LOGIN_CREDENTIALS, NEGATIVE_LOGIN_CREDENTIALS
from pages.auth_page import AuthPage
from pages.blog_pages.main_page import MainPage


@pytest.mark.auth
class TestAuthorizationClass:
    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.auth_page = AuthPage(browser, url + Links.login)
        self.auth_page.open_page()
        self.blog_page = MainPage(browser, url + Links.blog)

    @allure.title("Проверяем авторизацию ")
    def test_login_positive(self, browser, url):
        self.auth_page.login_ui(POSITIVE_LOGIN_CREDENTIALS['email'], POSITIVE_LOGIN_CREDENTIALS['password'])
        assert self.auth_page.page_is_open(url + Links.profile)
        self.auth_page.check_user_authorization()

    @pytest.mark.parametrize("email, password",
                             NEGATIVE_LOGIN_CREDENTIALS, ids=["empty email", "empty password", "invalid email",
                                                              "unregistered user"])

    def test_login_negative(self, email, password, url):
        self.auth_page.login_ui(email, password)
        assert self.auth_page.page_is_open(url + Links.login)

    @pytest.mark.usefixtures("login")
    def test_logout(self):
        self.blog_page.open_page()

        self.auth_page.logout()

        self.blog_page.open_page()
        self.blog_page.check_impossibility_creating_post()
