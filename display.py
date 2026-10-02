from menu import menu


def print_header():
    print()
    print("=" * 50)
    print("             BURGER HOUSE")
    print("          FRESH FOOD EVERY DAY")
    print("=" * 50)


def print_menu():
    print()
    print("-" * 50)
    print("                    MENU")
    print("-" * 50)
    print("{:<8} {:<28} {:>10}".format("CODE", "ITEM", "PRICE"))

    for item_code in menu:
        item_name = menu[item_code][0]
        item_price = menu[item_code][1]

        print("{:<8} {:<28} ₱{:>9,.2f}".format(
            item_code, item_name, item_price
        ))

    print("-" * 50)


def print_receipt(orders, total, discount, final_total):
    print()
    print("=" * 60)
    print("                    BURGER HOUSE")
    print("                 OFFICIAL RECEIPT")
    print("=" * 60)
    print("{:<25} {:>5} {:>12} {:>12}".format(
        "ITEM", "QTY", "PRICE", "TOTAL"
    ))
    print("-" * 60)

    for item_code in orders:
        item_name = orders[item_code][0]
        quantity = orders[item_code][1]
        item_price = orders[item_code][2]
        item_total = quantity * item_price

        print("{:<25} {:>5} ₱{:>10,.2f} ₱{:>10,.2f}".format(
            item_name, quantity, item_price, item_total
        ))

    print("-" * 60)
    print("{:<45} ₱{:>10,.2f}".format("SUBTOTAL:", total))
    print("{:<45} ₱{:>10,.2f}".format("DISCOUNT:", discount))
    print("{:<45} ₱{:>10,.2f}".format("TOTAL:", final_total))
    print("=" * 60)
    print("             Thank you for ordering!")
    print("                  Please come again!")
    print("=" * 60)


def print_goodbye():
    print()
    print("Thank you for visiting Burger House!")
    print("Have a nice day!")