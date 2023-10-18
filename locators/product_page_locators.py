from selenium.webdriver.common.by import By


class ProductPageLocators:
    CART_BUTTON = (By.XPATH, '//*[@id="button-cart"]')
    SUCCESS_MESSAGE = (By.XPATH, '//*[@id="partcont"]/div/div[1]')
    PRODUCT_PRICE = (By.XPATH, '//*[@id="update_price"]')
    PLUS_BUTTON = (By.XPATH, '//*[@id="superplus"]')
    MINUS_BUTTON = (By.XPATH, '//*[@id="superminus"]')
    QUANTITY_FIELD = (By.CSS_SELECTOR, '#content > div > div > div.col-sm-6.product-right > div.cart > div.number > input.plus-minus')
    WISHLIST_BUTTON = (By.CSS_SELECTOR, '#content > div > div > div.col-sm-6.product-right > div.cart > div.btn-group > button:nth-child(1)')
    WISHLIST_SUCCESS = (By.XPATH, '//*[@id="partcont"]')
    TEST_BUTTON = (By.XPATH, '//*[@id="partcont"]/div/div[3]/a')