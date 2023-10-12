from selenium.webdriver.common.by import By


class ProductPageLocators:
    CART_BUTTON = (By.XPATH, '//*[@id="button-cart"]')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="partcont"]/div/div[1]')
    PRODUCT_PRICE = (By.XPATH, '//*[@id="update_price"]')
    PLUS_BUTTON = (By.XPATH, '//*[@id="superplus"]')
    MINUS_BUTTON = (By.XPATH, '//*[@id="superminus"]')
    WISHLIST_BUTTON = (By.XPATH, '//*[@id="content"]/div/div/div[2]/div[4]/div[2]/button[1]')
    WISHLIST_SUCCESS = (By.XPATH, '//*[@id="partcont"]')
