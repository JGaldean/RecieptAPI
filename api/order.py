class Order:
    _tax_rate = 0.0725

    def __init__(self):
        """ This creates and empty list of items"""
        self._items = []
    
    def get_items(self):
        """ This will return a list with all of the drinks in the order """
        return self._items
    
    def get_num_items(self):
        return len(self._items)
    
    def get_total(self):
        return sum(
            item.get_total_price() if hasattr(item, 'get_total_price') 
            else item.get_total() if hasattr(item, 'get_total') 
            else 0
            for item in self._items
        )
    
    def get_tax(self):
        return self.get_total() * self._tax_rate
    
    def get_receipt(self):
        """ This is the function that will actually create a receipt for the order """
        receipt_data = {
            "number_items" : len(self._items),
            "items" : [],
            "subtotal" : round(self.get_total(), 2),
            "tax" : round(self.get_tax(), 2),
            "grand_total" : round(self.get_total() + self.get_tax(), 2)
        }

        for i, item in enumerate(self._items, start = 1):
            item_data = {
                "number" : i,
                "type" : item.__class__.__name__.lower(),
                "name" : getattr(item, "get_type", lambda: "N/A")(),
                "description" : str(item),
                "total_cost": round(item.get_total_price() if hasattr(item, "get_total_price") else item.get_total(), 2)
            }
            receipt_data["items"].append(item_data)

        return receipt_data
    
    def add_item(self, item):
        """ This function will add a drink to the order """
        if isinstance(item, (Drink, Food, IceStorm)):
            self._items.append(item)
        else:
            raise ValueError("You can only add food or drinks or IceStorms to this order!")
    
    def remove_item(self, index):
        """ And this function will remove a drink from the order """
        if 0 <= index < len(self._items):
            self._items.pop(index)
        else:
            raise IndexError("Invalid Request, You cannot remove this")
