import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    locators = LoginPageLocators()

    @allure.step('correct fill all fields')
    def correct_fill_all_fields(self, email, password):
        with allure.step('filling fields'):
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        with allure.step('click submit button'):
            self.element_is_visible(self.locators.SUBMIT).click()
        current_url = self.driver.current_url
        return current_url

    @allure.step('incorrect fill all fields')
    def incorrect_fill_all_fields(self, email, password):
        with allure.step('filling fields'):
            self.element_is_visible(self.locators.EMAIL).send_keys(email)
            self.element_is_visible(self.locators.PASSWORD).send_keys(password)
        with allure.step('click submit button'):
            self.element_is_visible(self.locators.SUBMIT).click()
        warning_message = self.element_is_visible(self.locators.MESSAGE).text
        return warning_message
