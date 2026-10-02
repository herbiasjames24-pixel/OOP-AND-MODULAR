from menu import Menu
from order import Order


def print_header():
    print()
    print("=" * 50)
    print("             BURGER HOUSE")
    print("          FRESH FOOD EVERY DAY")
    print("=" * 50)


def ask_yes_no(question):
    answer = input(question).lower()
    return answer == "yes" or answer == "y"


def main():
    menu = Menu()
    order = Order(menu)

    print_header()
    menu.display()

    if not ask_yes_no("Would you like to order? (yes/no): "):
        print()
        print("Thank you for visiting Burger House!")
        print("Have a nice day!")
        return

    ordering = True

    while ordering:
        item_code = order.get_menu_item()

        if item_code != "":
            quantity = order.get_quantity()

            if quantity > 0:
                order.add_item(item_code, quantity)
                ordering = ask_yes_no("Would you like to order another item? (yes/no): ")
        else:
            print("Please choose a valid menu item.")

    if not order.is_empty():
        order.print_receipt()
    else:
        print("No items were ordered.")


if __name__ == "__main__":
    main()