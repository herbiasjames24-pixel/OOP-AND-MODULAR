from menu import menu


def ask_to_order():
    answer = input("Would you like to order? (yes/no): ").lower()
    return answer == "yes" or answer == "y"


def get_menu_item():
    item_code = input("Enter item code: ")

    if item_code in menu:
        return item_code
    else:
        print("Invalid item code.")
        return ""


def get_quantity():
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


def ask_for_another_item():
    answer = input("Would you like to order another item? (yes/no): ").lower()
    return answer == "yes" or answer == "y"