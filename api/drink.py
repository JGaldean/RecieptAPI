class Drink:
  _valid_bases = {"water", "sbrite", "pokecola", "Mr. Salt", "hill fog", "leaf wine"}
    _valid_flavors = {"lemon", "cherry", "strawberry", "mint", "blueberry", "lime"}
    _size_costs = {
        "small" : 1.50,
        "medium" : 1.75,
        "large" : 2.05,
        "mega" : 2.50
    }

    def __init__(self, size):
        """ This creates a drink without a base or any flavors """
        self._base = None
        self._flavors = set()
        self._size = None
        self._cost = 0.0
        self.set_size(size)

    def get_base(self):
        """ This function will return the base of a drink """
        return self._base
    
    def get_flavors(self):
        """ This function will return a list of flavors in a drink """
        return list(self._flavors)
    
    def get_num_flavors(self):
        """ This function will return the number of flavors in a drink """
        return len(self._flavors)
    
    def get_size(self):
        return self._size
    
    def get_total(self):
        return self._cost
    
    def set_base(self, base):
        """ This will set the base of a drink, and make sure that it is a valid base """
        if base in self._valid_bases:
            self._base = base
        else:
            raise ValueError(f"Invalid Base: {base}. Please pick a base from {self._valid_bases}.")
        
    def add_flavor(self, flavor):
        """ This will add a flavor to the drink assuming that it is a valid option """
        if flavor in self._valid_flavors:
            if flavor not in self._flavors:
                self._flavors.add(flavor)
                self._cost += 0.15
        else:
            raise ValueError(f"Invalid Flavor: {flavor}. Please pick a flavor from {self._valid_flavors}.")
    
    def set_flavors(self, flavors):
        """ This will set the flavor of the drink and replace the existing flavors """
        if all(flavor in self._valid_flavors for flavor in flavors):
            new_flavors = set(flavors) - self.flavors
            self._cost += 0.15 * len(new_flavors)
            self._flavors = set(flavors)
        else:
            invalid_flavors = {flavor for flavor in flavors if flavor not in self._valid_flavors}
            raise ValueError(f"Invalid Flavor. Please pick a flavor from {self._valid_flavors}.")

    def set_size(self, size):
        size = size.lower()

        if size in self._size_costs:
            self._size = size
            self._cost = self._size_costs[size] + 0.15 * len(self._flavors)
        else:
            raise ValueError(f"Invalid Size. Please pick a different size : {list(self._size_costs.keys())}.")
