#Code Smells Example for long method
def calculate_total_price(items):
    total = 0
    for item in items:
        if item.quantity > 0:
            discount_multiplier = 0.9 if item.price > 100 else 0.95
            total += item.price * discount_multiplier
    return total
