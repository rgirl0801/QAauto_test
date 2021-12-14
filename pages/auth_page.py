from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# класс для работы со страницей авторизации (/login)

class AuthPage(BasePage):
    EMAIL_FIELD = (By.NAME, 'email')
    PASSWORD_FIELD = (By.NAME, 'password')
    BUTTON = (By.CLASS_NAME, 'button')

    def login_ui(self, email: str, password: str) -> None:
        """Функция логина на стенде через UI"""
        self.wait_until_clickable(self.EMAIL_FIELD).send_keys(email)
        self.wait_until_clickable(self.PASSWORD_FIELD).send_keys(password)
        self.wait_until_clickable(self.BUTTON).click()

    def check_user_authorization(self):
        assert self.browser.get_cookie('session'), 'Отсуствует куки session'
