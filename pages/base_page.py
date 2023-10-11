import allure
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.url = url

    # @allure.step('Open a browser')
    def open(self):
        self.driver.get(self.url)
    #
    # @allure.step('Find a visible element')
    # def element_is_visible(self, locator, timeout=5):
    #     self.go_to_element(self.element_is_present(locator))
    #     return wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
    #
    # @allure.step('Find visible elements')
    # def elements_are_visible(self, locator, timeout=5):
    #     return wait(self.driver, timeout).until(EC.visibility_of_all_elements_located(locator))
    #
    # @allure.step('Find a present element')
    # def element_is_present(self, locator, timeout=5):
    #     return wait(self.driver, timeout).until(EC.presence_of_element_located(locator))
    #
    # @allure.step('Find clickable elements')
    # def element_is_clickable(self, locator, timeout=5):
    #     return wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
    #
    # @allure.step('Go to specified element')
    # def go_to_element(self, element):
    #     self.driver.execute_script("arguments[0].scrollIntoView();", element)
    #
    def get_title(self):
        return self.driver.title
