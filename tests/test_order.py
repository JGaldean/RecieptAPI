import unittest
from api.order import Order
from api.drink import Drink
from api.food import Food
from api.icestorm import IceStorm

class TestOrder(unittest.TestCase):
    def setUp(self):
        """ Sets up a basic order to test """
        self.drink1 = Drink("small")
        self.drink1.set_base("water")
        self.drink1.add_flavor("lemon")

        self.drink2 = Drink("medium")
        self.drink2.set_base("sbrite")
        self.drink2.add_flavor("cherry")

        self.order = Order()
        self.order.add_item(self.drink1)
        self.order.add_item(self.drink2)

    def test_get_items(self):
        """ Tests the get_items """
        self.assertEqual(len(self.order.get_items()), 2)

    def test_get_total(self):
        """ tests get_total """
        self.assertAlmostEqual(self.order.get_total(), 3.55, places = 2)
    
    def test_get_tax(self):
        """ tests the get_tax """
        self.assertAlmostEqual(self.order.get_tax(), 0.26, places = 2)

    def test_get_num_items(self):
        """ tests get_num_items """
        self.assertEqual(self.order.get_num_items(), 2)

    def test_get_receipt(self):
        """ tests the get_receipt method """
        receipt = self.order.get_receipt()
        self.assertEqual(receipt["number_items"], 2)
        self.assertAlmostEqual(receipt["subtotal"], 3.55, places = 2)
        self.assertAlmostEqual(receipt["tax"], 0.26, places = 2)
        self.assertAlmostEqual(receipt["grand_total"], 3.81, places = 2)

    def test_add_invalid_item(self):
        """ tests adding an invalid item to the order """
        with self.assertRaises(ValueError):
            self.order.add_item("NOT_REAL_DRINK")

    def test_remove_item(self):
        """ Tests removing an item """
        self.order.remove_item(0)
        self.assertEqual(len(self.order.get_items()), 1)

    def test_remove_invalid_item(self):
        """ Tests the removing of an invalid items """
        with self.assertRaises(IndexError):
            self.order.remove_item(10)
