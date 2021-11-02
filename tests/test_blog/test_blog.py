import pytest
from selenium.webdriver.common.by import By

from api.api_helpers import delete_all_posts
from api.blog_api import BlogApi
from constants import Links
from functions import wait_until_clickable, wait_until_visible, element_is_present


@pytest.fixture()
def delete_user_posts(url):
    yield
    delete_all_posts(url)


@pytest.fixture()
def generate_post(url, faker):
    title_post = faker.text(10)
    text_post = faker.text(30)
    tags_post = faker.text(5)
    api = BlogApi(url)
    api.create_post(title=title_post, text=text_post, tags=tags_post)
    return title_post, text_post


@pytest.mark.usefixtures("delete_user_posts")
class TestsBlogOpen:
    def test_open_post(self, browser, url, generate_post):
        browser.get(url + Links.blog)
        text_title, text_post = generate_post
        wait_until_clickable(browser,
                             (By.XPATH, f'//h1[text()="{text_title}"]')).click()
        text_find = wait_until_visible(browser, (By.CSS_SELECTOR, ".container p+p"))

        assert text_post == text_find.text, "Неверный приветственный текст"


@pytest.mark.usefixtures("delete_user_posts")
class TestsBlogModify:
    def test_create_post(self, browser, url, faker):
        browser.get(url + Links.blog)
        wait_until_clickable(browser, (By.ID, "new")).click()
        title = faker.text(10)
        wait_until_clickable(browser, (By.ID, "title")).send_keys(title)
        wait_until_clickable(browser, (By.ID, "text")).send_keys(faker.text(100))
        wait_until_clickable(browser, (By.ID, "tags")).send_keys(faker.text(5))
        wait_until_clickable(browser, (By.ID, "submit")).click()

        assert "Blog posted successfully!" in wait_until_visible(browser, (By.ID, "alert_div")).text, \
            "Не отобразилось сообщение об успехе"
        assert wait_until_visible(browser, (By.TAG_NAME, "h1")).text == title, "Пост не опубликовался"

    def test_edit_post(self, browser, url, generate_post):
        browser.get(url + Links.blog)
        post_title = generate_post[0]
        cut_text_title =  post_title[:-1]
        wait_until_clickable(browser,
                             (By.XPATH, f'//h1[text()="{text_title}"]')).click()
        wait_until_clickable(browser, (By.ID, 'edit')).click()
        wait_until_clickable(browser, (By.CLASS_NAME, 'form-control')).send_keys(Keys.BACKSPACE)
        wait_until_clickable(browser, (By.ID, 'submit')).click()
        assert wait_until_clickable(browser, (By.XPATH, f'//h1[text()="{cut_text_title}"]')).text == cut_text_title

    def test_delete_post(self, browser, url, generate_post):
        browser.get(url + Links.blog)
        text_title = generate_post[0]
        delete_text = '×\nYour post was successfully deleted'
        wait_until_clickable(browser, (By.XPATH, f'//h1[text()="{text_title}"]')).click()
        wait_until_clickable(browser, (By.ID, 'delete')).click()
        wait_until_clickable(browser, (By.ID, 'confirmedDelete')).click()
        assert wait_until_clickable(browser, (By.XPATH, '//*[@id="alert_div"]')).text == delete_text
        assert not element_is_present(browser, (By.XPATH, f'//h1[text()="{text_title}"]'))
