class Order:

    def __init__(self, menu):
        self.menu = menu
        self.items = {}

    def get_menu_item(self):
        item_code = input("Enter item code: ")

        if self.menu.has_item(item_code):
            return item_code
        else:
            print("Invalid item code.")
            return ""

    def get_quantity(self):
        quantity_text = input("Enter quantity: ")

        if quantity_text.isdigit():
            quantity = int(quantity_text)

            if quantity > 0:
                return quantity
            else:
                print("Quantity must be greater than zero.")
                return 0
        else:
            print("Invalid quantity.")
            return 0

    def add_item(self, item_code, quantity):
        item_name, item_price = self.menu.get_item(item_code)

        if item_code in self.items:
            self.items[item_code][1] += quantity
        else:
            self.items[item_code] = [item_name, quantity, item_price]

    def is_empty(self):
        return len(self.items) == 0

    def calculate_total(self):
        total = 0

        for item_code in self.items:
            total += self.items[item_code][1] * self.items[item_code][2]

        return total

    def calculate_discount(self):
        total = self.calculate_total()

        if total >= 1000:
            return total * 0.10
        elif total >= 500:
            return total * 0.05
        else:
            return 0

    def print_receipt(self):
        total = self.calculate_total()
        discount = self.calculate_discount()
        final_total = total - discount

        print()
        print("=" * 60)
        print("                    BURGER HOUSE")
        print("                 OFFICIAL RECEIPT")
        print("=" * 60)
        print("{:<25} {:>5} {:>12} {:>12}".format(
            "ITEM", "QTY", "PRICE", "TOTAL"
        ))
        print("-" * 60)

        for item_code in self.items:
            item_name = self.items[item_code][0]
            quantity = self.items[item_code][1]
            item_price = self.items[item_code][2]

            print("{:<25} {:>5} ₱{:>10,.2f} ₱{:>10,.2f}".format(
                item_name, quantity, item_price, quantity * item_price
            ))

        print("-" * 60)
        print("{:<45} ₱{:>10,.2f}".format("SUBTOTAL:", total))
        print("{:<45} ₱{:>10,.2f}".format("DISCOUNT:", discount))
        print("{:<45} ₱{:>10,.2f}".format("TOTAL:", final_total))
        print("=" * 60)
        print("             Thank you for ordering!")
        print("                  Please come again!")
        print("=" * 60)