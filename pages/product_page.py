import time

import allure
from selenium.webdriver import ActionChains

from locators.login_page_locators import LoginPageLocators
from locators.product_page_locators import ProductPageLocators
from pages.base_page import BasePage


class ProductPage(BasePage):
    locators = ProductPageLocators()
    locators_authorized = LoginPageLocators()

    @allure.step('click cart button')
    def check_cart_button(self):
        self.element_is_present(self.locators.CART_BUTTON).click()
        text_title = self.element_is_present(self.locators.SUCCESS_MESSAGE).text
        return text_title

    @allure.step('click plus button')
    def check_plus_button(self):
        self.element_is_present(self.locators.PLUS_BUTTON).click()
        time.sleep(0.1)
        text = self.element_is_present(self.locators.PRODUCT_PRICE).text
        return text

    @allure.step('click minus button')
    def check_minus_button(self):
        self.element_is_present(self.locators.PLUS_BUTTON).click()
        time.sleep(0.1)
        self.element_is_present(self.locators.MINUS_BUTTON).click()
        time.sleep(0.1)
        text = self.element_is_present(self.locators.PRODUCT_PRICE).text
        return text

    @allure.step('authorization')
    def authorization(self):
        email = 'vladimirstepankin@mail.ru'
        password = 'Qwerty1234'
        with allure.step('filling fields'):
            self.element_is_visible(self.locators_authorized.EMAIL).send_keys(email)
            self.element_is_visible(self.locators_authorized.PASSWORD).send_keys(password)
        with allure.step('click submit button'):
            self.element_is_visible(self.locators_authorized.SUBMIT).click()

    @allure.step('click wishlist button')
    def check_wishlist_button(self):
        self.element_is_present(self.locators.WISHLIST_BUTTON).click()
        text = self.element_is_visible(self.locators.WISHLIST_SUCCESS)
        return text.is_displayed()
