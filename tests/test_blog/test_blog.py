import pytest

from QAauto_test.constants import Links


@pytest.mark.auth
class TestBlogClass:

    @pytest.mark.blog
    def test_blog(self, browser):
        browser.maximize_window()
        browser.get(Links.author)
        browser.find_element_by_xpath("//a[@href='/blog/page/1/test-post/']").click()
        assert browser.find_element_by_xpath("//p[2]").text == 'Hello world!'
