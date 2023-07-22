from pages.base_page import BasePage
from pages.locators import LoginPageLocators


class LoginPage(BasePage):

    def __init__(self, browser, url):
        super().__init__(browser, url)

    def should_be_login_url(self):
        assert "login" in self._url, "'url' doesn't contain 'login'"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not present"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not present"

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def register_new_user(self, email, password):
        email_field = self._browser.find_element(*LoginPageLocators.EMAIL_FIELD)
        email_field.send_keys(email)

        password_field = self._browser.find_element(*LoginPageLocators.PASSWORD_FIELD)
        password_field.send_keys(password)

        confirm_password_field = self._browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD)
        confirm_password_field.send_keys(password)

        submit_button = self._browser.find_element(*LoginPageLocators.REGISTER_SUBMIT)
        submit_button.click()
