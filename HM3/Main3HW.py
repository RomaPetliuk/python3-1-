from Rectangleclass import Rectangle
r = Rectangle
def calculate_area(x, y):
    return x * y

def calculate_perimeter(x, y):
    return 2 * (x + y)

print(calculate_area(r.width, r.height))
print(calculate_perimeter(r.width, r.height))