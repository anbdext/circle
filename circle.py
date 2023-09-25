import math

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * (self.r**2)

    def perimeter(self):
        return 2 * math.pi * self.r

# Get the radius from user input
radius = float(input("Enter radius: "))

# Create an instance of the Circle class
circle1 = Circle(radius)

# Calculate and print area and perimeter
print("Area is:", circle1.area())
print("Perimeter is:", circle1.perimeter())
