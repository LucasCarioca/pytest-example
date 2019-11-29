from enum import Enum


class PaymentService:
    def __init__(self):
        self.url = 'localhost:8080'
        self.user = 'username'
        self.password = 'password'
        self.sub_total = 0
        self.rate = 1.0

    def set_sub_total(self, sub_total):
        self.sub_total = sub_total

    def set_tax_rate(self, rate):
        self.rate = 1 + (rate/100)

    def process(self):
        print ('charging ${}'.format(self.calc_taxes()))
        return PaymentResults.SUCCESS

    def calc_taxes(self):
        return self.sub_total * self.rate


class PaymentResults(Enum):
    SUCCESS = 1
    DECLINED = 2
    ERROR = 2
