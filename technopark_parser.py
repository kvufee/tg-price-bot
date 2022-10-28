import re
from typing import Union
from parser import Parser
from item import Item
from bs4 import BeautifulSoup as soup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

class TechnoparkParser(Parser):
    def __init__(self, product_name: str, price: Union[float, int], url: str) -> None:
        self.product_name = product_name
        self.price = price
        self.url = url

    def scraping(self):
        driver = webdriver.Chrome(ChromeDriverManager.install())
        driver.get(self.url)
        searchbar = driver.find_element(By.XPATH, '//*[@id="header-search-input-main"]')
        searchbar.send_keys(self.url + Keys.RETURN)
        search = driver.find_element(By.CLASS_NAME, 'header-search-input__buttons')
        search.click()
        
        case_data = soup.find_all('div', attrs={'class':'product-card-big__container'})
        item_data = []

        for data in case_data:

            title = soup.find(attrs={"class":{"product-card-big__name"}}).get_text()
            price = soup.find_all(attrs={"class":{"product-prices__price"}}).get_text()
            url = "https://technopark.ru" + soup.find(attrs={"class":{"href"}})
            picture = soup.find(attrs={"class":{"tp-lazy-image product-card-image__img"}})
        
        item_data.append(Item(product_name=title, price=price, url=url, pic_url=picture))

        return item_data