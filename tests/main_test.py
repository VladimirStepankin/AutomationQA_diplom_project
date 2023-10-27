import allure
import yaml

from pages.main_page import MainPage


@allure.feature('Главная страница')
class TestMainPage:
    """Тесты главной страницы"""
    with open("./config.yaml") as f:
        data = yaml.safe_load(f)

    url = data["url"]

    @allure.title('Проверка заголовка')
    def test_main_page(self, driver):
        main_page = MainPage(driver, self.url)
        main_page.open()
        assert main_page.get_title() == 'GoAqua.ru - аквариумный интернет-магазин', "Page not found"

    @allure.title('Проверка элементов навигационного меню')
    def test_menu_items(self, driver):
        menu_page = MainPage(driver, self.url)
        menu_page.open()
        data = menu_page.check_menu()
        assert data == ['ОСВЕЩЕНИЕ', 'СО2 ОБОРУДОВАНИЕ', 'ФИЛЬТРАЦИЯ', 'УДОБРЕНИЯ И ПРЕПАРАТЫ', 'ИНСТРУМЕНТЫ',
                        'ВСЕ КАТЕГОРИИ'], "Menu items do not exist or have not been selected"

    @allure.title('Проверка редиректа в VK')
    def test_vk_tab(self, driver):
        browser_windows_page = MainPage(driver, self.url)
        browser_windows_page.open()
        text_result = browser_windows_page.check_opened_vk()
        assert text_result == 'GoAqua.ru Природный аквариум', "The tab has not opened or an incorrect tab has opened"

    @allure.title('Проверка редиректа в Youtube')
    def test_youtube_tab(self, driver):
        browser_windows_page = MainPage(driver, self.url)
        browser_windows_page.open()
        text_result = browser_windows_page.check_opened_youtube()
        assert text_result == 'GoAqua', "The tab has not opened or an incorrect tab has opened"

    @allure.title('Проверка редиректа в Whatsapp')
    def test_whatsapp_tab(self, driver):
        browser_windows_page = MainPage(driver, self.url)
        browser_windows_page.open()
        text_result = browser_windows_page.check_opened_whatsapp()
        assert text_result == 'GoAqua.ru', "The tab has not opened or an incorrect tab has opened"

    @allure.title('Проверка редиректа в Telegram')
    def test_telegram_tab(self, driver):
        browser_windows_page = MainPage(driver, self.url)
        browser_windows_page.open()
        text_result = browser_windows_page.check_opened_telegram()
        assert text_result == 'GoAqua', "The tab has not opened or an incorrect tab has opened"
