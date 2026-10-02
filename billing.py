def calculate_total(orders):
    total = 0

    for item_code in orders:
        quantity = orders[item_code][1]
        item_price = orders[item_code][2]
        total = total + (quantity * item_price)

    return total


def calculate_discount(total):
    if total >= 1000:
        return total * 0.10
    elif total >= 500:
        return total * 0.05
    else:
        return 0