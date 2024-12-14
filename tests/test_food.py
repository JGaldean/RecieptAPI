import unittest
from api.food import Food, Order

class TestFood(unittest.TestCase):
    def setUp(self):
        """ this creates basic food to test """
        self.food1 = Food("french fries")
        self.food2 = Food("hotdog")

    def test_get_type(self):
        """ Tests the get_type method """
        self.assertEqual(self.food1.get_type(), "french fries")
        self.assertEqual(self.food2.get_type(), "hotdog")

    def test_get_base_price(self):
        """ tests the get_base_price """
        self.assertAlmostEqual(self.food1.get_base_price(), 1.50)
        self.assertAlmostEqual(self.food2.get_base_price(), 2.30)

    def test_add_topping(self):
        """ tests adding VALID toppings """
        self.food1.add_topping("ketchup")
        self.food1.add_topping("nacho cheese")
        self.assertIn("ketchup", self.food1.get_toppings())
        self.assertIn("nacho cheese", self.food1.get_toppings())

    def test_get_num_toppings(self):
        """ tests getting the number of toppings """
        self.food1.add_topping("chili")
        self.assertEqual(self.food1.get_num_toppings(), 1)
        self.food1.add_topping("bacon bits")
        self.assertEqual(self.food1.get_num_toppings(), 2)

    def test_get_total_price(self):
        """ test the total_price with toppings """
        self.food1.add_topping("chili")
        self.food1.add_topping("bacon bits")
        self.assertAlmostEqual(self.food1.get_total_price(), 2.40)

    def test_invalid_topping(self):
        """ tests adding an INVALID topping """
        with self.assertRaises(ValueError):
            self.food1.add_topping("invalid_topping")

class TestOrderWithFood(unittest.TestCase):
    def setUp(self):
        """ creates an order with food items to test """
        self.order = Order()
        self.food1 = Food("french fries")
        self.food2 = Food("hotdog")
        self.food1.add_topping("ketchup")
        self.food1.add_topping("nacho cheese")
        self.food2.add_topping("chili")
        self.order.add_item(self.food1)
        self.order.add_item(self.food2)

    def test_get_items(self):
        """ this tests getting items from an order """
        items = self.order.get_items()
        self.assertEqual(len(items), 2)
        self.assertEqual(items[0].get_type(), "french fries")
        self.assertEqual(items[1].get_type(), "hotdog")

    def test_get_total(self):
        """ tests getting the total calculation """
        self.assertAlmostEqual(self.order.get_total(), 4.70)

    def test_get_receipt(self):
        """ tests generating a reciept """
        receipt = self.order.get_receipt()
        self.assertEqual(receipt["number_items"], 2)
        self.assertEqual(receipt["items"][0]["type"], "food")
        self.assertEqual(receipt["items"][0]["name"], "french fries")
        self.assertAlmostEqual(receipt["items"][0]["total_cost"], 1.80)
        self.assertEqual(receipt["items"][1]["type"], "food")
        self.assertEqual(receipt["items"][1]["name"], "hotdog")
        self.assertAlmostEqual(receipt["items"][1]["total_cost"], 2.90)

if __name__ == "__main__":
    unittest.main()
