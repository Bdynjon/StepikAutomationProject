from selenium.common.exceptions import NoSuchElementException


class BasePage:
    def __init__(self, browser, url, timeout=10):
        self._browser = browser
        self._browser.implicitly_wait(timeout)
        self._url = url

    def open(self):
        self._browser.get(self._url)

    def is_element_present(self, how, what):
        try:
            self._browser.find_element(how, what)
        except NoSuchElementException:
            return False
        return True
