import allure
from selenium.webdriver import ActionChains

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    """Главная страница"""
    locators = MainPageLocators()

    @allure.step('проверить навигационное меню сайта')
    def check_menu(self):
        menu_item_list = self.locators.MENU_ITEM_LIST
        data = []
        action = ActionChains(self.driver)

        for locator in menu_item_list:
            element = self.driver.find_element(*locator)
            action.move_to_element(element).perform()
            data.append(element.text)
        return data

    @allure.step('проверить переход на VK')
    def check_opened_vk(self):
        self.element_is_visible(self.locators.VK_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.VK_TITLE).text
        return text_title

    @allure.step('проверить переход на YOUTUBE')
    def check_opened_youtube(self):
        self.element_is_visible(self.locators.YOUTUBE_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.YOUTUBE_TITLE).text
        return text_title

    @allure.step('проверить переход в WHATSAPP')
    def check_opened_whatsapp(self):
        self.element_is_visible(self.locators.WHATSAPP_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.WHATSAPP_TITLE).text
        return text_title

    @allure.step('проверить переход в TELEGRAM')
    def check_opened_telegram(self):
        self.element_is_visible(self.locators.TELEGRAM_BUTTON).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text_title = self.element_is_present(self.locators.TELEGRAM_TITLE).text
        return text_title
