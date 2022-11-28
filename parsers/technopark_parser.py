from typing import Union, List
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

from .parser import Parser
from item import Item
import configuration.config as cfg


class TechnoparkParser(Parser):

    def __init__(self) -> None:
        self.url = 'https://technopark.ru'


    def scraping(self, product_name: str) -> List[str]:
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(self.url)
        searchbar = driver.find_element(By.XPATH, '//*[@id="header-search-input-main"]')
        searchbar.send_keys(product_name)
        searchbar.send_keys(Keys.RETURN)

        time.sleep(cfg.SLEEP_DURATION)

        page_content = driver.page_source
        soup = BeautifulSoup(page_content, 'lxml')

        containers = soup.find_all('div', attrs={'class':'product-card-big__container'})
        
        items = []

        for container in containers:
            url = 'https://technopark.ru' + container.find('a')['href']
            title = container.find('a')['title']
            price = container.find('div', attrs={'class':'product-prices__price'}).get_text()
            pic = container.find('img', attrs={'class':'tp-lazy-image product-card-image__img'})

            items.append(Item(url=url, product_name=title, price=price, pic_url=pic))
        
        return items