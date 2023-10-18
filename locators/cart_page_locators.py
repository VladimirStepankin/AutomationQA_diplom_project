from selenium.webdriver.common.by import By


class CartPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, '#simplecheckout_cart > div.table-responsive > table > tbody > tr > td.name > a')
    MODEL = (By.CSS_SELECTOR, '#simplecheckout_cart > div.table-responsive > table > tbody > tr > td.model')
    MINUS_BUTTON = (By.CSS_SELECTOR, '#simplecheckout_cart > div.table-responsive > table > tbody > tr > td.quantity > div > span:nth-child(1) > button')
    PLUS_BUTTON = (By.CSS_SELECTOR, '#simplecheckout_cart > div.table-responsive > table > tbody > tr > td.quantity > div > span:nth-child(3) > button.btn.btn-primary')
    QUANTITY_FIELD = (By.CSS_SELECTOR, '#simplecheckout_cart > div.table-responsive > table > tbody > tr > td.quantity > div > input')
    REMOVE_BUTTON = (By.CSS_SELECTOR, '#simplecheckout_cart > div.table-responsive > table > tbody > tr > td.quantity > div > span:nth-child(3) > button.btn.btn-danger')
    EMPTY_CART_MESSAGE = (By.CSS_SELECTOR, '#simplecheckout_form_0 > div > div.content')
