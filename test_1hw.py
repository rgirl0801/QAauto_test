import pytest
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By

from functions import login, wait_for_url_to_be, wait_until_clickable
from auth import data


@pytest.mark.auth
class TestAuthorizationClass:

    @pytest.mark.smoke
    def test_login_positive(self):
        with Chrome() as browser:
            browser.get('https://qastand.valhalla.pw/login')  # step1
            browser.maximize_window()
            login(browser)  # step 2,3,4
            wait_for_url_to_be(browser, 'https://qastand.valhalla.pw/profile')  # step5
            assert browser.get_cookie("session"), 'Отсуствует куки session'  # step6


    @pytest.mark.parametrize("email, password",
                             data.values(), ids=data.keys())
    
    def test_login_negative(self, email, password):
        with Chrome() as browser:
            browser.get('https://qastand.valhalla.pw/login')  # step1
            browser.maximize_window()
            wait_until_clickable(browser, (By.NAME, "email")).send_keys(email)  # step2
            wait_until_clickable(browser, (By.NAME, "password")).send_keys(password)  # step2
            wait_until_clickable(browser, (By.CLASS_NAME, "button")).click()  # step3
            assert wait_for_url_to_be(browser, 'https://qastand.valhalla.pw/login'), 'Произошла авторизация'  # step4
