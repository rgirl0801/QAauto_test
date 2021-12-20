from typing import Tuple

import allure
from selenium.common.exceptions import TimeoutException
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebElement
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


# класс с общими хэлперами и методами для работы с элементами, которые расположены на каждой странице


class BasePage:
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "[href = '/logout']")

    def __init__(self, browser: Chrome, url):
        self.browser = browser
        self.url = url

    def open_page(self):
        self.browser.get(self.url)

    @allure.step("Ждём, пока URL страницы не начнёт соответствовать ожидаемому")
    def wait_for_url_to_be(self, url: str, timeout: int = 5) -> bool:
        return WebDriverWait(self.browser, timeout).until(ec.url_to_be(url))

    @allure.step("Ждём, пока заголовок веб-страницы (title) не начнёт соответствовать ожидаемому")
    def page_title_is(self, title: str, timeout: int = 5) -> bool:
        return WebDriverWait(self.browser, timeout).until(ec.title_is(title))

    @allure.step("Ждём, пока элемент не станет видимым и кликабельным")
    def wait_until_clickable(self, locator: Tuple, timeout: int = 5) -> WebElement:
        return WebDriverWait(self.browser, timeout).until(ec.element_to_be_clickable(locator))

    @allure.step("Ждём, пока элемент не появится в DOM")
    def wait_until_present(self, locator: Tuple, timeout: int = 5) -> WebElement:
        return WebDriverWait(self.browser, timeout).until(ec.presence_of_element_located(locator))

    @allure.step("Ждём, когда элемента не будет на странице")
    def wait_until_not_present(self, locator: Tuple, timeout=5) -> WebElement:
        return WebDriverWait(self.browser, timeout).until_not(ec.presence_of_element_located(locator))

    @allure.step("Ждём, пока элемент не станет видимым")
    def wait_until_visible(self, locator: Tuple, timeout: int = 5):
        return WebDriverWait(self.browser, timeout).until(ec.visibility_of_element_located(locator))

    @allure.step("Убеждаемся, что элемент присутствует на странице")
    def element_is_present(self, locator: Tuple, timeout: int = 5) -> bool:
        try:
            self.wait_until_visible(locator, timeout)
            return True
        except TimeoutException:
            return False

    @allure.step("Проверяем возможность выхода")
    def logout(self):
        self.wait_until_clickable(self.LOGOUT_BUTTON).click()

    @allure.step("Проверяем открывается ли страница")
    def page_is_open(self, url):
        try:
            self.wait_for_url_to_be(url)
            return True
        except TimeoutException:
            return False
