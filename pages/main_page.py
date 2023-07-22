from pages.base_page import BasePage
from pages.locators import MainPageLocators
from selenium.webdriver.common.by import By


class MainPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def go_to_login_page(self):
        login_link = self._browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
