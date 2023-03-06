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
