class Rectangle:
    def __init__(self):
        self.width = int(input("Write width of the rectangle: "))
        self.height = int(input("Write height of the rectangle: "))

    def calculate_area(self):
        return self.width * self.height

    def calculate_perimeter(self):
        return 2 * (self.width + self.height)