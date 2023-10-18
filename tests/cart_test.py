import os
import time
import yaml
import allure

from pages.cart_page import CartPage
from pages.product_page import ProductPage


@allure.feature('Cart Page')
class TestCartPage:
    url_of_cart = 'https://goaqua.ru/simplecheckout/'
    url_of_product = 'https://goaqua.ru/osveshchenie/svetodiodnye-svetilniki/chihiros-wrgb-ii-pro-series/svetilnik-chihiros-wrgb-ii-pro-120.html'
    url_of_autorization = 'https://goaqua.ru/login/'
    # file_path = os.path.join(os.path.dirname(__file__), "../config.yaml")
    with open("../config.yaml") as f:
        data = yaml.safe_load(f)
    email = data['email']
    password = data['password']

    @allure.title('Check title')
    def test_cart_page(self, driver):
        cart_page = CartPage(driver, self.url_of_cart)
        cart_page.open()
        title = cart_page.get_title()
        assert title == 'Оформление заказа'

    @allure.step('Check product name on cart')
    def test_product_name(self, driver, ):
        cart_page = CartPage(driver, self.url_of_autorization)
        cart_page.open()
        cart_page.authorization(self.email, self.password)
        driver.get(self.url_of_product)
        cart_page.put_product_in_cart()
        name = cart_page.check_product_name()
        assert name == 'Светильник Chihiros WRGB II PRO 120'

    @allure.step('Check product model on cart')
    def test_product_model(self, driver, ):
        cart_page = CartPage(driver, self.url_of_autorization)
        cart_page.open()
        cart_page.authorization(self.email, self.password)
        driver.get(self.url_of_product)
        cart_page.put_product_in_cart()
        name = cart_page.check_product_model()
        assert name == '391-11201'

    @allure.title('Check plus button')
    def test_plus_button(self, driver):
        cart_page = CartPage(driver, self.url_of_autorization)
        cart_page.open()
        cart_page.authorization(self.email, self.password)
        driver.get(self.url_of_product)
        cart_page.put_product_in_cart()

        # value = cart_page.check_plus_button()
        # assert value == '2'

    # @allure.title('Check minus button')
    # def test_plus_button(self, driver):
    #     product_page = ProductPage(driver, self.url_of_product)
    #     product_page.open()
    #     coast = product_page.check_minus_button()
    #     assert coast == '40 000.00 р.'