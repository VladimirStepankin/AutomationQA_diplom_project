import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    """Страница авторизации"""
    locators = LoginPageLocators()

    @allure.step('корректно заполнить все поля')
    def correct_fill_all_fields(self, email, password):
        with allure.step('заполнение полей'):
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        with allure.step('клик на кнопку "Войти"'):
            self.element_is_visible(self.locators.SUBMIT).click()
        current_url = self.driver.current_url
        return current_url

    @allure.step('некорректно заполнить все поля')
    def incorrect_fill_all_fields(self, email, password):
        with allure.step('заполнение полей'):
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        with allure.step('клик на кнопку "Войти"'):
            self.element_is_visible(self.locators.SUBMIT).click()
        warning_message = self.element_is_visible(self.locators.MESSAGE).text
        return warning_message
