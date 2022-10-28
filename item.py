from typing import Union

class Item:
    def __init__(self, product_name: str, price: Union[float, int], url: str, pic_url: str) -> None:
        self.product_name = product_name
        self.price = price
        self.url = url
        self.pic_url = pic_url