from src.checkout import Checkout
from unittest.mock import MagicMock
import pytest
import sys
import random
sys.path.insert(0, '../src')


@pytest.fixture()
def checkout():
    checkout = Checkout()
    return checkout


def test_checkout_can_add_item(checkout):
    checkout.add_item('ItemA')


def test_checkout_can_add_item_and_price(checkout):
    checkout.add_item_w_price('ItemA', 100)


def test_checkout_can_calc_total(checkout):
    price = random.randint(1, 10000)
    checkout.add_item_w_price('ItemA', price)
    assert checkout.calc_total() == price


def test_checkout_can_calc_total_multi_item(checkout):
    price_list = [random.randint(1, 10000) for _ in range(1, 100)]
    for price in price_list:
        checkout.add_item_w_price('item{}'.format(price), price)
    assert checkout.calc_total() == sum(price_list)


def test_checkout_can_calc_total_w_discounts(checkout):
    discount_price = random.randint(1, 100)
    price = random.randint(101, 10000)
    checkout.add_item_w_price('ItemA', price)
    price2 = random.randint(101, 10000)
    checkout.add_item_w_price('ItemA', price2)
    checkout.add_discount('ItemA', discount_price)
    assert checkout.calc_total() == discount_price*2


def test_checkout_should_set_sub_total_in_payment_service_when_pay_is_requested(checkout):
    mock_payment_service = MagicMock()
    mock_payment_service.set_sub_total = MagicMock()
    checkout.payment_service = mock_payment_service

    price_list = [random.randint(1, 10000) for _ in range(1, 100)]
    for price in price_list:
        checkout.add_item_w_price('item{}'.format(price), price)

    checkout.pay()
    mock_payment_service.set_sub_total.assert_called_once_with(sum(price_list))


def test_checkout_should_process_using_payment_service_when_pay_is_requested(checkout):
    mock_payment_service = MagicMock()
    mock_payment_service.process = MagicMock()
    checkout.payment_service = mock_payment_service

    price_list = [random.randint(1, 10000) for _ in range(1, 100)]
    for price in price_list:
        checkout.add_item_w_price('item{}'.format(price), price)

    checkout.pay()
    mock_payment_service.process.assert_called_once()
