from selenium.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
import pytest


def pytest_addoption(parser):
    parser.addoption("--language", action="Store", default="en", help="Choose language")


@pytest.fixture()
def browser(request):

    language = request.getoption("language")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": language})

    browser = Chrome(options=options)
    yield browser

    browser.quit()
