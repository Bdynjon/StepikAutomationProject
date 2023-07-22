class BasePage:
    def __int__(self, browser, url):
        self._browser = browser
        self._url = url

    def open(self):
        self._browser.get(self._url)
