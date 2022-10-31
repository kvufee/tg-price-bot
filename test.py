from item import Item
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get('https://www.technopark.ru/search/?q=iphone%2013&withContent=true&strategy=vectors_extended,zero_queries')
searchbar = driver.find_element(By.XPATH, '//*[@id="header-search-input-main"]')
searchbar.send_keys('Iphone 13')
searchbar.send_keys(Keys.RETURN)

page_content = driver.page_source
soup = BeautifulSoup(page_content, 'lxml')

containers = soup.find_all('div', attrs={'class':'product-card-big__container'})

items = []
for container in containers:

    url = 'https://technopark.ru' + container.find('a')['href']
    title = container.find('a')['title']
    price = container.find('div', attrs={'class':'product-prices__price'}).get_text()
    pic = container.find('img', attrs={'class':'tp-lazy-image product-card-image__img'})
    items.append(Item(url=url, product_name=title, price=price, pic_url = pic))

print(items)