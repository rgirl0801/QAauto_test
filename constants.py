from selenium.webdriver import Opera, Chrome, Remote

NEGATIVE_LOGIN_CREDENTIALS = [
    ("", "!QAZ2wsx"),
    ("qa_test@test.ru", ""),
    ("qa_test", "!QAZ2wsx"),
    ("test@test.ru", "1QAZ2wsx")
]

# здесь должны быть креденшелзы, присланные преподавателем
POSITIVE_LOGIN_CREDENTIALS = {"email": "api_user_11@test.ru",
                              "password": "q11w11e11"}


class Links:
    base_url = {"prod": "https://qastand.valhalla.pw/",
                "stage": "https://qastand-dev.valhalla.pw/"}
    login = "login"
    profile = "profile"
    blog = "blog"


VALID_BROWSERS = {
    "chrome": Chrome,
    "opera": Opera,
    "remote": Remote
}
BROWSER_REMOTE_CAPABILITIES = {
    "browserName": "chrome",
    "version": "95.0",
    "enableVNC": True,
}
COMMAND_EXECUTOR = {"ci": "http://selenoid-chrome:4444",
                    "local": "http://localhost:4444/wd/hub"}


ТЕСТ ТЕСТ