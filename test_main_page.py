import pytest

from pages.main_page import MainPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


def test_guest_can_go_to_login_page(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, url)
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.open()
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    url = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, url)
    page.open()
    page.should_be_login_link()


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
