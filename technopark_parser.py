from typing import Union
from parser import Parser
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TechnoparkParser(Parser):
    def __init__(self, product_name: str, price: Union[float, int], url: str) -> None:
        self.product_name = product_name
        self.price = price
        self.url = url

    def scraping(self) -> str:
        driver = webdriver.Chrome(ChromeDriverManager.install())
        driver.get(self.url)
        