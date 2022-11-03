from item import Item

from typing import List, Union
from abc import ABC, abstractclassmethod

class Parser(ABC):


    @abstractclassmethod
    def item_list(self, product_name: str) -> List[str]:
        pass

    def requested_item_data(self, 
                            product_name: str,
                            price: Union[int, float], 
                            url: str) -> Item:
        
        return Item(product_name=product_name, price=price, url=url)
