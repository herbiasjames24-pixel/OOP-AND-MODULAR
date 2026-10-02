class Menu:

    def __init__(self):
        self.items = {
            "1": ["Big Mac Meal", 185],
            "2": ["Chicken Nuggets", 135],
            "3": ["Bacon Cheeseburger", 160],
            "4": ["Chicken Sandwich", 150],
            "5": ["Large French Fries", 85],
            "6": ["Chocolate Sundae", 75],
            "7": ["Apple Pie", 65],
            "8": ["Iced Tea", 55]
        }

    def has_item(self, item_code):
        return item_code in self.items

    def get_item(self, item_code):
        return self.items[item_code]

    def display(self):
        print()
        print("-" * 50)
        print("                    MENU")
        print("-" * 50)
        print("{:<8} {:<28} {:>10}".format("CODE", "ITEM", "PRICE"))

        for item_code in self.items:
            item_name = self.items[item_code][0]
            item_price = self.items[item_code][1]

            print("{:<8} {:<28} ₱{:>9,.2f}".format(
                item_code, item_name, item_price
            ))

        print("-" * 50)