class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_price(self, discount_list):
        if self.name in discount_list:
            return discount_list[self.name].discounted_price
        else:
            return self.price
