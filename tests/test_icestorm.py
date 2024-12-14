import unittest
from Drink_Assignment import IceStorm

class TestIceStorm(unittest.TestCase):
    def setUp(self):
        """ Sets up an IceStorm for testing """
        self.ice_storm = IceStorm(size="medium")

    def test_add_flavor(self):
        """ Tests adding valid flavors """
        self.ice_storm.add_flavor("Chocolate")
        self.ice_storm.add_flavor("Mint Chocolate Chip")
        self.assertEqual(self.ice_storm.get_flavors(), ["Chocolate", "Mint Chocolate Chip"])

    def test_add_invalid_flavor(self):
        """ Tests adding an invalid flavor """
        with self.assertRaises(ValueError):
            self.ice_storm.add_flavor("Invalid Flavor")

    def test_add_topping(self):
        """ Tests adding valid toppings """
        self.ice_storm.add_topping("Cherry")
        self.ice_storm.add_topping("Cookie Dough")
        self.assertEqual(self.ice_storm.get_toppings(), ["Cherry", "Cookie Dough"])

    def test_add_invalid_topping(self):
        """ Tests adding an invalid topping """
        with self.assertRaises(ValueError):
            self.ice_storm.add_topping("Invalid Topping")

    def test_get_size(self):
        """ Tests getting the size """
        self.assertEqual(self.ice_storm.get_size(), "medium")

    def test_get_num_flavors(self):
        """ Tests getting the number of flavors """
        self.ice_storm.add_flavor("Vanilla Bean")
        self.ice_storm.add_flavor("Banana")
        self.assertEqual(self.ice_storm.get_num_flavors(), 2)

    def test_get_total(self):
        """ Tests calculating the total cost """
        self.ice_storm.add_flavor("Chocolate")
        self.ice_storm.add_flavor("Vanilla Bean")
        self.ice_storm.add_topping("Cherry")
        self.ice_storm.add_topping("Pecans")
        self.assertAlmostEqual(self.ice_storm.get_total(), 8.00, places=2)

    def test_string_representation(self):
        """ Tests the IceStorm representations """
        self.ice_storm.add_flavor("S'more")
        self.ice_storm.add_topping("Whipped Cream")
        self.assertEqual(str(self.ice_storm), "IceStorm (Size: medium, Base: Ice Cream Base, Flavors: [S'more], Toppings: [Whipped Cream], Total: $5.50)")

if __name__ == "__main__":
    unittest.main()
