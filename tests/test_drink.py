import unittest
from api.drink import Drink

class TestDrink(unittest.TestCase):
    def setUp(self):
        """ Creates a basic drink for the testing """
        self.drink = Drink("small")
        self.drink.set_base("water")
        self.drink.add_flavor("lemon")

    def test_get_base(self):
        """ This tests the get_base method """
        self.assertEqual(self.drink.get_base(), "water")
    
    def test_get_flavor(self):
        """ This tests the get_flavor """
        self.assertEqual(self.drink.get_flavors(), ["lemon"])

    def test_get_num_flavors(self):
        """ Tests the get_num_flavors """
        self.assertEqual(self.drink.get_num_flavors(), 1)

    def test_get_size(self):
        """ Tests the method get_size """
        self.assertEqual(self.drink.get_size(), "small")

    def test_get_total(self):
        """ tests get_total """
        self.assertAlmostEqual(self.drink.get_total(), 1.65, places = 2)

    def test_invalid_base(self):
        """ Tests an invalid base setting """
        with self.assertRaises(ValueError):
            self.drink.set_base("invalid_base")

    def test_invalid_flavor(self):
        """ Tests an invalid flavor """
        with self.assertRaises(ValueError):
            self.drink.add_flavor("invalid_flavor")
