import pytest
from pages.product_page import ProductPage

N = list(range(10))
N[7] = pytest.param(7, marks=pytest.mark.xfail)


@pytest.mark.parametrize('n', N)
def test_guest_can_add_product_to_basket(browser, n):
    url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{n}"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page.should_be_correct_product_name()
    page.should_be_correct_product_cost()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=NewYear"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=NewYear"
    page = ProductPage(browser, url)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    url = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=NewYear"
    page = ProductPage(browser, url)
    page.open()
    page.add_to_basket()
    page.solve_quiz_and_get_code()

    page.should_success_message_disappeared()
