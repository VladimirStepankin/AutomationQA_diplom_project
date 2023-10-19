import allure

from pages.product_page import ProductPage


@allure.feature('Страница товара')
class TestProductPage:
    """Тесты страницы товара"""

    email = 'vladimirstepankin@mail.ru'
    password = 'Qwerty1234'
    url_prod = 'https://goaqua.ru/osveshchenie/svetodiodnye-svetilniki/chihiros-wrgb-ii-pro-series/svetilnik-chihiros-wrgb-ii-pro-120.html'
    url_login = 'https://goaqua.ru/login/'

    @allure.title('Проверка заголовка')
    def test_product_page(self, driver):
        product_page = ProductPage(driver, self.url_prod)
        product_page.open()
        title = product_page.get_title()
        assert title == 'Светильник Chihiros WRGB II PRO 120 - купить на GoAqua.ru', "Page not found"

    @allure.title('Проверка добавления товара в корзину')
    def test_cart_button(self, driver):
        product_page = ProductPage(driver, self.url_prod)
        product_page.open()
        title = product_page.check_cart_button()
        assert title == 'Товар успешно добавлен в корзину!', "The product has not been added to the cart"

    @allure.title('Проверка уменьшения количества товара')
    def test_minus_button(self, driver):
        product_page = ProductPage(driver, self.url_prod)
        product_page.open()
        value = product_page.check_minus_button()
        assert value == '1', "Pinus button is faulty"

    @allure.title('Проверка увеличения количества товара')
    def test_plus_button(self, driver):
        product_page = ProductPage(driver, self.url_prod)
        product_page.open()
        value = product_page.check_plus_button()
        assert value == '2', "Plus button is faulty"

    @allure.title('Проверка добавления товара в закладки')
    def test_wishlist_button(self, driver):
        product_page = ProductPage(driver, self.url_login)
        product_page.open()
        product_page.authorization(self.email, self.password)
        driver.get(self.url_prod)
        text = product_page.check_wishlist_button()
        assert text is True, "The product has not been added to the wishlist"
