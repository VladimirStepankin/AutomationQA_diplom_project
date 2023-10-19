import time
import allure

from locators.cart_page_locators import CartPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.product_page_locators import ProductPageLocators
from pages.base_page import BasePage


class CartPage(BasePage):
    """Страница корзины"""
    locators = CartPageLocators()
    locators_authorized = LoginPageLocators()
    locators_product = ProductPageLocators()

    @allure.step('авторизоваться')
    def authorization(self, email, password):
        with allure.step('заполнение полей'):
            self.element_is_visible(self.locators_authorized.EMAIL).send_keys(email)
            self.element_is_visible(self.locators_authorized.PASSWORD).send_keys(password)
        with allure.step('клик на кнопку "Войти"'):
            self.element_is_visible(self.locators_authorized.SUBMIT).click()

    @allure.step('положить товар в корзину')
    def put_product_in_cart(self):
        self.element_is_present(self.locators_product.CART_BUTTON).click()
        self.element_is_visible(self.locators_product.TEST_BUTTON).click()

    @allure.step('проверить наименование товара')
    def check_product_name(self):
        text = self.element_is_visible(self.locators.PRODUCT_NAME).text
        return text

    @allure.step('проверить модель товара')
    def check_product_model(self):
        text = self.element_is_visible(self.locators.MODEL).text
        return text

    @allure.step('кликнуть на кнопку "+"')
    def check_plus_button(self):
        self.element_is_present(self.locators.PLUS_BUTTON).click()
        time.sleep(0.1)
        value = self.element_is_clickable(self.locators.QUANTITY_FIELD).get_attribute("value")
        return value

    @allure.step('кликнуть на кнопку "-"')
    def check_minus_button(self):
        self.element_is_present(self.locators.PLUS_BUTTON).click()
        time.sleep(0.1)
        self.element_is_clickable(self.locators.MINUS_BUTTON).click()
        time.sleep(0.1)
        value = self.element_is_clickable(self.locators.QUANTITY_FIELD).get_attribute("value")
        return value

    @allure.step('кликнуть на кнопку "удалить"')
    def check_remove_button(self):
        self.element_is_present(self.locators.REMOVE_BUTTON).click()
        time.sleep(0.1)
        text = self.element_is_visible(self.locators.EMPTY_CART_MESSAGE).text
        return text
