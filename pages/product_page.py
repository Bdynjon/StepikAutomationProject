from pages.base_page import BasePage
from pages.locators import ProductPageLocators


class ProductPage(BasePage):
    def __init__(self, browser, url):
        super().__init__(browser, url)

    def add_to_basket(self):
        add_to_basket_button = self._browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()

    def should_be_correct_product_name(self):
        product_name = self._browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_name_result = self._browser.find_element(*ProductPageLocators.PRODUCT_NAME_RESULT).text
        assert product_name == product_name_result, "Wrong product was bought"

    def should_be_correct_product_cost(self):
        product_cost = self._browser.find_element(*ProductPageLocators.PRODUCT_COST).text
        product_cost_result = self._browser.find_element(*ProductPageLocators.PRODUCT_COST_RESULT).text
        assert product_cost == product_cost_result, "Wrong product cost was calculated"
