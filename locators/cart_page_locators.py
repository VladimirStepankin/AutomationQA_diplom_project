from selenium.webdriver.common.by import By


class CartPageLocators:
    PRODUCT_NAME = (By.CSS_SELECTOR, '#simplecheckout_cart > div.table-responsive > table > tbody > tr > td.name > a')
    MODEL = (By.CSS_SELECTOR, '#simplecheckout_cart > div.table-responsive > table > tbody > tr > td.model')
    MINUS_BUTTON = (By.XPATH, '//*[@id="simplecheckout_cart"]/div[1]/table/tbody/tr/td[4]/div/span[1]')
    PLUS_BUTTON = (By.XPATH, '//*[@id="simplecheckout_cart"]/div[1]/table/tbody/tr/td[4]/div/span[2]')
    QUANTITY_FIELD = (By.XPATH, '//*[@id="simplecheckout_cart"]/div[1]/table/tbody/tr/td[4]/div/input')
    REMOVE_BUTTON = (By.XPATH, '//*[@id="simplecheckout_cart"]/div[1]/table/tbody/tr/td[4]/div/span[2]/button[2]')
    EMPTY_CART_MESSAGE = (By.XPATH, '//*[@id="simplecheckout_form_0"]/div/div[1]')
