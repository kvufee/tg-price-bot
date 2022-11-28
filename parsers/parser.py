from typing import List, Union
from abc import ABC, abstractclassmethod

from item import Item


class Parser(ABC):

    @abstractclassmethod
    def scraping(self, product_name: str) -> List[str]:
        pass