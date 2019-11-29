from src.models.item import Item
from src.models.discount import Discount
from src.services.payment import PaymentService, PaymentResults

class Checkout:

    def __init__(self):
        self.cart = []
        self.discount_list = {}
        self.payment_service = PaymentService()

    def add_item_w_price(self, item, price):
        self.cart.append(Item(item,price))

    def add_item(self, item):
        self.cart.append(Item(item, 0))

    def calc_total(self):
        return sum([item.get_price(self.discount_list) for item in self.cart if item.price > 0])

    def add_discount(self, item, discount_price):
        self.discount_list[item] = Discount(item, discount_price)

    def pay(self):
        self.payment_service.set_sub_total(self.calc_total())
        return self.payment_service.process()
