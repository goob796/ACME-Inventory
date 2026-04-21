#CashRegister class

class CashRegister:
    def __init__(self):
        self.cart = []

    def purchase_item(self, item):
        self.cart.append(item)

    def get_total(self):
        total = 0
        for item in self.cart:
            total += item.get_price()
        return total

    def get_cart(self):
        if not self.cart:
            print("Cart is empty.")
        else:
            print("\nItems in Cart:")
            for i, item in enumerate(self.cart, start=1):
                print(f"{i}. {item}")

    def empty(self):
        self.cart.clear()