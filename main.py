from display import print_header, print_menu, print_receipt, print_goodbye
from user_input import ask_to_order, get_menu_item, get_quantity, ask_for_another_item
from orders import add_order
from billing import calculate_total, calculate_discount


def main():
    orders = {}

    print_header()
    print_menu()

    if not ask_to_order():
        print_goodbye()
        return

    ordering = True

    while ordering:
        item_code = get_menu_item()

        if item_code != "":
            quantity = get_quantity()

            if quantity > 0:
                add_order(orders, item_code, quantity)
                ordering = ask_for_another_item()
        else:
            print("Please choose a valid menu item.")

    if len(orders) > 0:
        total = calculate_total(orders)
        discount = calculate_discount(total)
        final_total = total - discount
        print_receipt(orders, total, discount, final_total)
    else:
        print("No items were ordered.")


if __name__ == "__main__":
    main()