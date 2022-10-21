from typing import List, Union
from abc import ABC, abstractclassmethod

class Item:
    def __init__(self, product_name: str, price: Union[float, int], url: str, pic_url: str) -> None:
        self.product_name = product_name
        self.price = price
        self.url = url

class Parser(ABC):
    @abstractclassmethod
    def item_list(self, product_name: str) -> List[str]:
        pass

    def item_data_input(self, product_name, price, url: str) -> Item:
        return Item(product_name=product_name, price=price, url=url)