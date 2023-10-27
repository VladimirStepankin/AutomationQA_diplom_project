import time
import allure

from locators.login_page_locators import LoginPageLocators
from locators.product_page_locators import ProductPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):
    """Страница товара"""
    locators = ProductPageLocators()
    locators_authorized = LoginPageLocators()

    @allure.step('добавить товар в корзину')
    def check_cart_button(self):
        self.element_is_present(self.locators.CART_BUTTON).click()
        text_title = self.element_is_present(self.locators.SUCCESS_MESSAGE).text
        return text_title

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

    @allure.step('авторизоваться')
    def authorization(self, email, password):
        with allure.step('заполнение полей'):
            self.element_is_visible(self.locators_authorized.EMAIL).send_keys(email)
            self.element_is_visible(self.locators_authorized.PASSWORD).send_keys(password)
        with allure.step('клик на кнопку "Войти"'):
            self.element_is_visible(self.locators_authorized.SUBMIT).click()

    @allure.step('добавить товар в закладки')
    def check_wishlist_button(self):
        self.element_is_present(self.locators.WISHLIST_BUTTON).click()
        text = self.element_is_visible(self.locators.WISHLIST_SUCCESS)
        return text.is_displayed()
