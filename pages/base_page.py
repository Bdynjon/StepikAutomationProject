class BasePage:
    def __init__(self, browser, url):
        self._browser = browser
        self._url = url

    def open(self):
        self._browser.get(self._url)
