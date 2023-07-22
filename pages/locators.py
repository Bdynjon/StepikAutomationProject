from selenium.webdriver.common.by import By


class BasketPageLocators:
    BASKET_ITEMS = (By.CSS_SELECTOR, "div.basket-items")


class BasePageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    BASKET_LINK = (By.CSS_SELECTOR, "div.basket-mini a")
    USER_ICON = (By.CSS_SELECTOR, "i.icon-user")


class LoginPageLocators:
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL_FIELD = (By.CSS_SELECTOR, "input[name='registration-email']")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='registration-password1']")
    CONFIRM_PASSWORD_FIELD = (By.CSS_SELECTOR, "input[name='registration-password2']")
    REGISTER_SUBMIT = (By.CSS_SELECTOR, "button[name='registration_submit']")


class ProductPageLocators:
    ADD_TO_BASKET_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_NAME_RESULT = (By.CSS_SELECTOR, "div[id='messages'] div:nth-child(1) strong")
    PRODUCT_COST_RESULT = (By.CSS_SELECTOR, "div[id='messages'] div:nth-child(3) strong")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_COST = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "div[id='messages'] div:nth-child(1)")
