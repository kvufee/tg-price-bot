from typing import Union, List
import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from .parser import Parser
from item import Item
import configuration.config as cfg

class MvideoParser(Parser):
    
    def __init__(self) -> None:
        self.url = 'https://www.mvideo.ru/'
    
    def scraping(self, product_name: str) -> List[Item]:
        options = Options()

        with webdriver.Chrome(ChromeDriverManager().install()) as driver:
            driver.get(self.url)

            time.sleep(cfg.SLEEP_DURATION)

            searchbar = driver.find_element(By.XPATH, '//*[@id="1"]')
            searchbar.send_keys(product_name)
            searchbar.send_keys(Keys.RETURN)

            page_content = driver.page_source

        soup = BeautifulSoup(page_content, 'lxml')

        containers = soup.find_all('div', attrs={'class':'ng-star-inserted product-cards-row'})

        items = []

        for container in containers:
            url = self.url + container.find('a')