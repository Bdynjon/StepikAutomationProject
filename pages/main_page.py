from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def go_to_login_page(self):
        login_link = self._browser.find_element(By.CSS_SELECTOR, "#login_link")
        login_link.click()
