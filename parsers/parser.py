from item import Item

from typing import List, Union
from abc import ABC, abstractclassmethod


class Parser(ABC):

    @abstractclassmethod
    def scraping(self, product_name: str) -> List[str]:
        pass