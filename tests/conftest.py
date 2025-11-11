import pytest
from utils.Chrome import Chrome
from utils.Firefox import Firefox
from utils.Edge import Edge


@pytest.fixture(params=["chrome", "firefox", "edge"], scope="class")
def browser_instance(request):
    url = "https://dzen.ru/"
    browser = None
    if request.param == "chrome":
        browser = Chrome(url)
    elif request.param == "firefox":
        browser = Firefox(url)
    elif request.param == "edge":
        browser = Edge(url)
    request.cls.browser = browser
    browser.driver.maximize_window()
    yield browser
    browser.driver.quit()
