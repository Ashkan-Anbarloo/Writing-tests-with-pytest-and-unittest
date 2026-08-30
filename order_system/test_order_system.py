import unittest
from .order_system import *

class TestProduct(unittest.TestCase):
    def test_product_availability(self):
        p = Product('keyborad' , price=100 , stock=5)

        self.assertTrue(p.is_available(3))
        self.assertFalse(p.is_available(11))

    def test_reduce_stock_success(self):
        p = Product('Monitor' , price=300 , stock=4)
        p.reduce_stock(2)
        self.assertEqual(p.stock , 2)

    def test_reduce_stock_failure(self):
        p = Product('Camera' , 500 , 1)
        with self.assertRaises(ValueError):
            p.reduce_stock(3)


class TestOrderItem(unittest.TestCase):
    def setUp(self):
        self.p = Product('Mouse' , 50 , 10)

    def test_create_order_item(self):
        item = OrderItem(self.p , 3)
        self.assertEqual(item.quantity , 3)
        self.assertEqual(item.price , 150)
        self.assertEqual(self.p.stock , 7)

    def test_create_order_item_invalid_quantity(self):
        with self.assertRaises(ValueError):
            OrderItem(self.p , 0)
        with self.assertRaises(ValueError):
            OrderItem(self.p , -1)

    def test_create_order_item_invalid_stock(self):
        with self.assertRaises(ValueError):
            OrderItem(self.p , 120)

class TestOrder(unittest.TestCase):
    def setUp(self):
        self.p1 = Product('laptop' , 1000 , 3)
        self.p2 = Product('Headphone' , 200 , 5)
        self.order = Order()

    def test_add_item(self):
        self.order.add_item(self.p1 , quantity=2)
        self.assertEqual(self.order.item_count() , 1)
        self.assertEqual(self.p1.stock , 1)

    def test_add_multiple_items(self):
        self.order.add_item(self.p1 , quantity=1)
        self.order.add_item(self.p2 , quantity=2)
        self.assertEqual(self.order.total_price(), 1400)

    def test_add_item_stock(self):
        with self.assertRaises(ValueError):
            self.order.add_item(self.p1 , quantity=10)

    def test_total_price_empty_order(self):
        self.assertEqual(self.order.total_price(), 0)

