#Code Smells Example for long method
def calculate_total_price(items):
    total = 0
    for item in items:
        price=item.price
        if item.quantity > 0:
            if item.price > 100:
                price *= 0.9
            else:
                price *= 0.95
        total += price
    return total
