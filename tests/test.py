import os
import time
import yaml
from selenium.webdriver.common.by import By
import  configparser
from locators.product_page_locators import ProductPageLocators
from pages.product_page import ProductPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


if __name__ == '__main__':
    # file_path = os.path.join(os.path.dirname(__file__), "../config.yaml")
    # file_path = "../config.yaml"
    data = None
    with open("../config.yaml") as f:
        data = yaml.safe_load(f)
    print(data)