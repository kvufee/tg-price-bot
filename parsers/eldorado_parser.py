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


class EldoradoParser(Parser):

    def __init__(self) -> None:
        self.url = 'https://www.eldorado.ru'

    def scraping(self, product_name: str) -> List[Item]:

        with webdriver.Chrome(ChromeDriverManager().install()) as driver:
            driver.get(self.url)

            time.sleep(cfg.SLEEP_DURATION)

            searchbar = driver.find_element(By.XPATH, '//*[@id="search-form"]/div[1]/input')
            searchbar.send_keys(product_name)
            searchbar.send_keys(Keys.RETURN)
            
            time.sleep(cfg.INPUT_DURATION)

            page_content = driver.page_source

        soup = BeautifulSoup(page_content, 'lxml')

        containers = soup.find_all()

        items = []

        for container in containers:
            url = self.url + container.find('a').get('href')
            title = container.find('a', attrs={'class':'DE'}).text
            price = container.find('span', attrs={'class':'vR CR'}).text
            pic = container.find('img').get('src')

            items.append(Item(url=url, product_name=title, price=price, pic_url=pic))

        return items