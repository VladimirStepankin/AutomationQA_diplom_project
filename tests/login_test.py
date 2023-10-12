import allure

from pages.login_page import LoginPage


@allure.feature('Login Page')
class TestLoginPage:
    @allure.title('Check title')
    def test_login_page(self, driver):
        login_page = LoginPage(driver, 'https://goaqua.ru/login/')
        login_page.open()
        assert login_page.get_title() == 'Авторизация'

    @allure.title('Check correct fill all fields')
    def test_correct_fill(self, driver):
        login_page = LoginPage(driver, 'https://goaqua.ru/login/')
        login_page.open()
        url = login_page.correct_fill_all_fields()
        assert url == 'https://goaqua.ru/my-account/'

    @allure.title('Check incorrect fill all fields')
    def test_incorrect_fill(self, driver):
        login_page = LoginPage(driver, 'https://goaqua.ru/login/')
        login_page.open()
        text = login_page.incorrect_fill_all_fields()
        assert text == 'Неправильно заполнены поля E-Mail и/или пароль!'