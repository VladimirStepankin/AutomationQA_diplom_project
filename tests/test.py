import time

from selenium.webdriver.common.by import By

from locators.product_page_locators import ProductPageLocators
from pages.product_page import ProductPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


if __name__ == '__main__':
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    service = Service(executable_path=ChromeDriverManager().install())
    driver = webdriver.Chrome(service=service, options=options)
    product_page = ProductPage(driver,
                               'https://goaqua.ru/osveshchenie/svetodiodnye-svetilniki/chihiros-wrgb-ii-pro-series/svetilnik-chihiros-wrgb-ii-pro-120.html')
    product_page.open()

    card_button = driver.find_element(By.XPATH, '//*[@id="superplus"]')
    card_button.click()
    time.sleep(10)