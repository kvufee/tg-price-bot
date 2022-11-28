from typing import Union

class Item:

    def __init__(self, 
                 url: str, 
                 product_name: str, 
                 price: Union[float, int], 
                 pic_url: str) -> None:
        self.product_name = product_name
        self.price = price
        self.url = url
        self.pic_url = pic_url
    

    def __repr__(self) -> str:
        return f"{self.product_name}, {self.price}, {self.url}"
        