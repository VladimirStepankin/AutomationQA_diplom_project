import allure

from pages.cart_page import CartPage


@allure.feature('Страница корзины')
class TestCartPage:
    """Тесты страницы корзины"""

    email = 'vladimirstepankin@mail.ru'
    password = 'Qwerty1234'
    url_cart = 'https://goaqua.ru/simplecheckout/'
    url_auth = 'https://goaqua.ru/login/'
    url_prod = 'https://goaqua.ru/osveshchenie/svetodiodnye-svetilniki/chihiros-wrgb-ii-pro-series/svetilnik-chihiros-wrgb-ii-pro-120.html'

    @allure.title('Проверка заголовка')
    def test_cart_page(self, driver):
        cart_page = CartPage(driver, self.url_cart)
        cart_page.open()
        title = cart_page.get_title()
        assert title == 'Оформление заказа', "Page not found"

    @allure.step('Проверка наименования товара')
    def test_product_name(self, driver, ):
        cart_page = CartPage(driver, self.url_auth)
        cart_page.open()
        cart_page.authorization(self.email, self.password)
        driver.get(self.url_prod)
        cart_page.put_product_in_cart()
        name = cart_page.check_product_name()
        assert name == 'Светильник Chihiros WRGB II PRO 120', "Wrong product name"

    @allure.step('Проверка модели товара')
    def test_product_model(self, driver, ):
        cart_page = CartPage(driver, self.url_auth)
        cart_page.open()
        cart_page.authorization(self.email, self.password)
        driver.get(self.url_prod)
        cart_page.put_product_in_cart()
        model = cart_page.check_product_model()
        assert model == '391-11201', "Wrong product model"

    @allure.title('Проверка удаления товара')
    def test_remove_button(self, driver):
        cart_page = CartPage(driver, self.url_auth)
        cart_page.open()
        cart_page.authorization(self.email, self.password)
        driver.get(self.url_prod)
        cart_page.put_product_in_cart()
        text = cart_page.check_remove_button()
        assert text == "Ваша корзина пуста!", "Remove button is faulty"

    @allure.title('Проверка уменьшения количества товара')
    def test_minus_button(self, driver):
        cart_page = CartPage(driver, self.url_auth)
        cart_page.open()
        cart_page.authorization(self.email, self.password)
        driver.get(self.url_prod)
        cart_page.put_product_in_cart()
        value = cart_page.check_minus_button()
        assert value == '1', "Minus button is faulty"

    @allure.title('Проверка увеличения количества товара')
    def test_plus_button(self, driver):
        cart_page = CartPage(driver, self.url_auth)
        cart_page.open()
        cart_page.authorization(self.email, self.password)
        driver.get(self.url_prod)
        cart_page.put_product_in_cart()
        value = cart_page.check_plus_button()
        assert value == '3', "Plus button is faulty"
