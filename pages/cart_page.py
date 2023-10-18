import time

import allure
from selenium.webdriver import ActionChains

from locators.cart_page_locators import CartPageLocators
from locators.login_page_locators import LoginPageLocators
from locators.product_page_locators import ProductPageLocators
from pages.base_page import BasePage


class CartPage(BasePage):
    locators = CartPageLocators()
    locators_authorized = LoginPageLocators()
    locators_product = ProductPageLocators()

    @allure.step('authorization')
    def authorization(self, email, password):
        with allure.step('filling fields'):
            self.element_is_visible(self.locators_authorized.EMAIL).send_keys(email)
            self.element_is_visible(self.locators_authorized.PASSWORD).send_keys(password)
        with allure.step('click submit button'):
            self.element_is_visible(self.locators_authorized.SUBMIT).click()

    @allure.step('put product in cart')
    def put_product_in_cart(self):
        self.element_is_present(self.locators_product.CART_BUTTON).click()
        self.element_is_visible(self.locators_product.TEST_BUTTON).click()

    @allure.step('check product name')
    def check_product_name(self):
        text = self.element_is_visible(self.locators.PRODUCT_NAME).text
        return text

    @allure.step('check product model')
    def check_product_model(self):
        text = self.element_is_visible(self.locators.MODEL).text
        return text

    @allure.step('click plus button')
    def check_plus_button(self):
        self.element_is_present(self.locators.PLUS_BUTTON).click()
        time.sleep(0.1)
        text = self.element_is_present(self.locators.QUANTITY_FIELD).text
        return text

    @allure.step('click minus button')
    def check_minus_button(self):
        self.element_is_present(self.locators.PLUS_BUTTON).click()
        time.sleep(0.1)
        self.element_is_present(self.locators.MINUS_BUTTON).click()
        time.sleep(0.1)
        value = self.element_is_present(self.locators.QUANTITY_FIELD).get_attribute("value")
        return value

    @allure.step('click remove button')
    def check_remove_button(self):
        self.element_is_present(self.locators.REMOVE_BUTTON).click()
        time.sleep(0.1)
        text = self.element_is_present(self.locators.EMPTY_CART_MESSAGE).text
        return text
