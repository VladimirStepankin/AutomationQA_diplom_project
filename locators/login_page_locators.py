from selenium.webdriver.common.by import By


class LoginPageLocators:
    EMAIL = (By.XPATH, '//*[@id="input-email"]')
    PASSWORD = (By.XPATH, '//*[@id="input-password"]')
    SUBMIT = (By.XPATH, '//*[@id="content"]/div/div[2]/div/form/input')
    MESSAGE = (By.XPATH, '//*[@id="container"]/div[2]')
