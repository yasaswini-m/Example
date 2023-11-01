#Duplicate code example
def calculate_area(length, width):
    return length * width


def calculate_perimeter(length, width):
    return 2 * (length + width)


def calculate_volume(length, width, height): 
    return calculate_area(length, width) * height


def calculate_surface_area(length, width, height):
    return 2 * (calculate_area(length, width) + calculate_area(length, height) + calculate_area(width, height))


# Duplicate code: calculate_area and calculate_perimeter functions have similar calculations.
def calculate_area_perimeter(length, width):
    return calculate_area(length, width), calculate_perimeter(length, width)
