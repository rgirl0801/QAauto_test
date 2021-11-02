import pytest
from selenium.webdriver.common.by import By

from constants import Links
from pages.base_page import BasePage
# класс для работы со страницей авторизации (/login)
from pages.blog_pages.main_page import MainPage
from pages.blog_pages.post_modify_page import PostModifyPage


class AuthPage(BasePage):
    EMAIL_FIELD = 'email'
    PASSWORD_FIELD = 'password'
    BUTTON = 'button'

    def login_ui(self, email: str, password: str) -> None:
        """Функция логина на стенде через UI"""
        self.wait_until_clickable((By.NAME, self.EMAIL_FIELD)).send_keys(email)
        self.wait_until_clickable((By.NAME, self.PASSWORD_FIELD)).send_keys(password)
        self.wait_until_clickable((By.NAME, self.BUTTON)).click()

    @pytest.fixture(autouse=True)
    def setup(self, browser, url):
        self.blog_page = MainPage(browser, url + Links.blog)
        self.post_modify_page = PostModifyPage(browser, url + Links.blog)


class AuthPageLocators(BasePage):
    ...
