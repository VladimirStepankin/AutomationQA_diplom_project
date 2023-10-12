import time

import allure

from pages.product_page import ProductPage


@allure.feature('Product Page')
class TestProductPage:
    url_of_product = 'https://goaqua.ru/osveshchenie/svetodiodnye-svetilniki/chihiros-wrgb-ii-pro-series/svetilnik-chihiros-wrgb-ii-pro-120.html'

    @allure.title('Check title')
    def test_product_page(self, driver):
        product_page = ProductPage(driver, self.url_of_product)
        product_page.open()
        title = product_page.get_title()
        assert title == 'Светильник Chihiros WRGB II PRO 120 - купить на GoAqua.ru'

    @allure.title('Check cart button')
    def test_cart_button(self, driver):
        product_page = ProductPage(driver, self.url_of_product)
        product_page.open()
        title = product_page.check_cart_button()
        assert title == 'Товар успешно добавлен в корзину!'

    @allure.title('Check plus button')
    def test_plus_button(self, driver):
        product_page = ProductPage(driver, self.url_of_product)
        product_page.open()
        coast = product_page.check_plus_button()
        assert coast == '80 000.00 р.'

    @allure.title('Check minus button')
    def test_plus_button(self, driver):
        product_page = ProductPage(driver, self.url_of_product)
        product_page.open()
        coast = product_page.check_minus_button()
        assert coast == '40 000.00 р.'

    @allure.title('Check wishlist button')
    def test_plus_button(self, driver):
        product_page = ProductPage(driver,
                                   'https://goaqua.ru/login/')
        product_page.open()
        product_page.authorization()
        driver.get(self.url_of_product)
        text = product_page.check_wishlist_button()
        assert text is True
