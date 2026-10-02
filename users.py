from menu import menu


def add_order(orders, item_code, quantity):
    item_name = menu[item_code][0]
    item_price = menu[item_code][1]

    if item_code in orders:
        orders[item_code][1] = orders[item_code][1] + quantity
    else:
        orders[item_code] = [item_name, quantity, item_price]