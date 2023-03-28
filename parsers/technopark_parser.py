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


class TechnoparkParser(Parser):

    def __init__(self) -> None:
        self.url = 'https://technopark.ru'


    def scraping(self, product_name: str) -> List[Item]:
        options = Options()
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36')
        options.add_argument('accept-encoding=gzip, deflate, br')
        options.add_argument("window-size=1920,1080")

        with webdriver.Chrome(ChromeDriverManager().install(), options=options) as driver:
            driver.get(self.url)
            
            time.sleep(cfg.SLEEP_DURATION)

            searchbar = driver.find_element(By.XPATH, '//*[@id="header-search-input-main"]')
            searchbar.click()
            searchbar.clear()
            searchbar.send_keys(product_name)
            searchbar.send_keys(Keys.ENTER)

            time.sleep(cfg.SLEEP_DURATION)
            
            scroll = False

            if scroll:
                for i in range(5):
                    time.sleep(0.2)
                    driver.execute_script(f"window.scrollTo({i * 300}, {(i+1)*300})") 

            page_content = driver.page_source

        soup = BeautifulSoup(page_content, 'lxml')

        containers = soup.find_all('div', attrs={'class':'product-card-big__container'})
                
        items = []

        for container in containers:
            url = self.url + container.find('a')['href']
            title = container.find('a')['title']
            price = container.find('div', attrs={'class':'product-prices__price'}).get_text()
            pic = container.find('img', attrs={'class':'tp-lazy-image product-card-image__img'})

            items.append(Item(url=url, product_name=title, price=price, pic_url=pic))
            
        return items
