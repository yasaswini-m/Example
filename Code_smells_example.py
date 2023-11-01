#Code Smells Example for long method
def calculate_total_price(items):
    total = 0
    for item in items:
        if item.quantity > 0:
            factor=0
            if item.price > 100:
                 factor= 0.9
            else:
                 factor= 0.95
        total += item.price * factor
    return total
