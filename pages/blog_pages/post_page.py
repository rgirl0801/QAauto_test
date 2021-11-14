from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


# класс для работы со страницей отображения поста (пример URL — /blog/page/1/test-post/ или /blog/page/1)
class PostPage(BasePage):
    POST_TEXT = (By.CSS_SELECTOR, ".container p+p")
    EDIT_BUTTON = (By.ID, 'edit')
    DELETE_BUTTON = (By.ID, 'delete')
    CONFIRM_DELETE_BUTTON = (By.ID, 'confirmedDelete')
    TITLE = (By.TAG_NAME, 'h1')
    EDIT_TITLE_FORM = (By.CLASS_NAME, 'form-control')
    SUBMIT_BUTTON = (By.ID, "submit")

    def check_post_text(self, text):
        post_text = self.wait_until_visible(self.POST_TEXT)
        assert post_text.text == text, "Неверный текст"

    def click_edit_button(self):
        self.wait_until_clickable(self.EDIT_BUTTON).click()

    def click_submit_button(self):
        self.wait_until_clickable(self.SUBMIT_BUTTON).click()

    def click_delete_button(self):
        self.wait_until_clickable(self.DELETE_BUTTON).click()

    def click_confirm_delete_button(self):
        self.wait_until_clickable(self.CONFIRM_DELETE_BUTTON).click()

    def check_title_is_changed(self, new_title):
        assert self.wait_until_visible(self.TITLE).text == new_title

    def edit_form_title(self):
        self.wait_until_clickable(self.EDIT_TITLE_FORM).send_keys(Keys.BACKSPACE)
