from pages.base_page import BasePage
from pages.main_page import MainPage


class TestMainPage:
    def test_main_page(self, driver):
        main_page = MainPage(driver, 'https://goaqua.ru/')
        main_page.open()
        assert main_page.get_title() == 'GoAqua.ru - аквариумный интернет-магазин'