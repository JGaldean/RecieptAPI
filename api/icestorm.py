class IceStorm:
    _flavor_prices = {
        "Mint Chocolate Chip" : 4.00,
        "Chocolate" : 3.00,
        "Vanilla Bean" : 3.00,
        "Banana" : 3.50,
        "Butter Pecan" : 3.50,
        "S'more" : 4.00
    }

    _topping_prices = {
        "Cherry" : 0.00,
        "Whipped Cream" : 0.00,
        "Caramel Sauce" : 0.50,
        "Chocolate Sauce" : 0.50,
        "Storios" : 1.00,
        "Dig Dogs" : 1.00,
        "T&T's" : 1.00,
        "Cookie Dough" : 1.00,
        "Pecans" : 0.50
    }

    _size_prices = {
        "small" : 1.00,
        "medium" : 1.50,
        "large" : 2.00
    }

    def __init__(self, size = "medium"):
        if size not in self._size_prices:
            raise ValueError(f"This is not a valid size")
        self._size = size
        self._flavors = []
        self._toppings = []
        self._base_cost = self._size_prices[size]

    def add_flavor(self, flavor):
        if flavor in self._flavor_prices:
            self._flavors.append(flavor)
            self._base_cost += self._flavor_prices[flavor]
        else:
            raise ValueError(f"This is not a valid flavor")
    
    def add_topping(self, topping):
        if topping in self._topping_prices:
            self._toppings.append(topping)
        else:
            raise ValueError(f"This is not a valid flavor")
    
    def get_flavors(self):
        return self._flavors

    def get_toppings(self):
        return self._toppings

    def get_base(self):
        return "Ice Cream Base"
    
    def get_size(self):
        return self._size

    def get_num_flavors(self):
        return len(self._flavors)

    def get_total(self):
    # Correct calculation
        flavor_cost = sum(self._flavor_prices[f] for f in self._flavors)
        topping_cost = sum(self._topping_prices[t] for t in self._toppings)
        size_cost = self._size_prices[self._size]  # Ensure size is only added once
        return flavor_cost + topping_cost + size_cost

    def __str__(self):
        flavors = ", ".join(f"[{flavor}]" for flavor in self._flavors)
        toppings = ", ".join(self._toppings)
        return f"IceStorm (Size: {self._size}, Base: {self.get_base()}, Flavors: {flavors}, Toppings: [{toppings}], Total: ${self.get_total():.2f})"
