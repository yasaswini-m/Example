def discount_multiplier(price):
    return 0.9 if price > 100 else 0.95

def calculate_total_price(items):
    total = 0
    for item in items:
        if item.quantity > 0:
            total += item.price * discount_multiplier(item.price)
    return total
