#Class RetailItem

class RetailItem:
    def __init__(self, description, units, price):
        self.__description = description
        self.__units = units
        self.__price = price

    # Accessors
    def get_description(self):
        return self.__description

    def get_units(self):
        return self.__units

    def get_price(self):
        return self.__price

    # Mutators
    def set_description(self, description):
        self.__description = description

    def set_units(self, units):
        self.__units = units

    def set_price(self, price):
        self.__price = price

    def __str__(self):
        return f"{self.__description}, Units: {self.__units}, Price: ${self.__price:.2f}"