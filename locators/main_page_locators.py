from selenium.webdriver.common.by import By


class MainPageLocators:
    HEADER_LOGO = (By.CSS_SELECTOR, 'img[class="img-responsive"')
    MENU_ITEM_LIST = [
        (By.XPATH, '//*[@id="megamenu-menu"]/div/div[3]/ul/li[1]/a[1]'),
        (By.XPATH, '//*[@id="megamenu-menu"]/div/div[3]/ul/li[2]/a[1]'),
        (By.XPATH, '//*[@id="megamenu-menu"]/div/div[3]/ul/li[3]/a[1]'),
        (By.XPATH, '//*[@id="megamenu-menu"]/div/div[3]/ul/li[4]/a[1]'),
        (By.XPATH, '//*[@id="megamenu-menu"]/div/div[3]/ul/li[5]/a[1]'),
        (By.XPATH, '//*[@id="megamenu-menu"]/div/div[3]/ul/li[6]/a[1]')
    ]
    VK_BUTTON = (By.XPATH, '/html/body/footer/div[1]/div/div/div[1]/div[3]/a[1]')
    VK_TITLE = (By.XPATH, '//*[@id="public"]/div[1]/div[2]/div[2]/div[1]/h1')
    YOUTUBE_BUTTON = (By.XPATH, '/html/body/footer/div[1]/div/div/div[1]/div[3]/a[2]')
    YOUTUBE_TITLE = (By.XPATH, '//*[@id="text"]')
    WHATSAPP_BUTTON = (By.XPATH, '/html/body/footer/div[1]/div/div/div[1]/div[3]/a[3]')
    WHATSAPP_TITLE = (By.XPATH, '//*[@id="main_block"]/div[1]/h3')
    TELEGRAM_BUTTON = (By.XPATH, '/html/body/footer/div[1]/div/div/div[1]/div[3]/a[4]')
    TELEGRAM_TITLE = (By.XPATH, '/html/body/div[2]/div[2]/div/div[1]/span')
