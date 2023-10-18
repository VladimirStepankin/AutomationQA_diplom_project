import allure

from pages.main_page import MainPage


@allure.feature('Menu Page')
class TestMainPage:
    url = 'https://goaqua.ru/'

    @allure.title('Check title')
    def test_main_page(self, driver):
        main_page = MainPage(driver, self.url)
        main_page.open()
        assert main_page.get_title() == 'GoAqua.ru - аквариумный интернет-магазин', "Page not found"

    @allure.title('Check all of the menu items')
    def test_menu_items(self, driver):
        menu_page = MainPage(driver, self.url)
        menu_page.open()
        data = menu_page.check_menu()
        assert data == ['ОСВЕЩЕНИЕ', 'СО2 ОБОРУДОВАНИЕ', 'ФИЛЬТРАЦИЯ', 'УДОБРЕНИЯ И ПРЕПАРАТЫ', 'ИНСТРУМЕНТЫ',
                        'ВСЕ КАТЕГОРИИ'], "menu items do not exist or have not been selected"

    @allure.title('Checking the opening of VK tab')
    def test_vk_tab(self, driver):
        browser_windows_page = MainPage(driver, self.url)
        browser_windows_page.open()
        text_result = browser_windows_page.check_opened_vk()
        assert text_result == 'GoAqua.ru Природный аквариум', "the tab has not opened or an incorrect tab has opened"

    @allure.title('Checking the opening of youtube tab')
    def test_youtube_tab(self, driver):
        browser_windows_page = MainPage(driver, self.url)
        browser_windows_page.open()
        text_result = browser_windows_page.check_opened_youtube()
        assert text_result == 'GoAqua', "the tab has not opened or an incorrect tab has opened"

    @allure.title('Checking the opening of whatsapp tab')
    def test_whatsapp_tab(self, driver):
        browser_windows_page = MainPage(driver, self.url)
        browser_windows_page.open()
        text_result = browser_windows_page.check_opened_whatsapp()
        assert text_result == 'GoAqua.ru', "the tab has not opened or an incorrect tab has opened"

    @allure.title('Checking the opening of telegram tab')
    def test_telegram_tab(self, driver):
        browser_windows_page = MainPage(driver, self.url)
        browser_windows_page.open()
        text_result = browser_windows_page.check_opened_telegram()
        assert text_result == 'GoAqua', "the tab has not opened or an incorrect tab has opened"
