class Rectangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def peri(self):
        return 2 * (self.length + self.breadth)

# Inputs
a = int(input("Enter length of first rectangle: "))
b = int(input("Enter breadth of first rectangle: "))
c = int(input("Enter length of second rectangle: "))
d = int(input("Enter breadth of second rectangle: "))

# Create objects
obj = Rectangle(a, b)
obj1 = Rectangle(c, d)

# Display
print("Area of first rectangle:", obj.area())
print("Perimeter of first rectangle:", obj.peri())
print("Area of second rectangle:", obj1.area())

# Compare area
if obj.area() > obj1.area():
    print("First rectangle has larger area")
elif obj.area() < obj1.area():
    print("Second rectangle has larger area")
else:
    print("Both rectangles have equal area")