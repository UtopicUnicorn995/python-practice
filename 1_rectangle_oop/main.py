

class Rectangle:
    def __init__(self, width, length):
        self.width = int(width)
        self.length = int(length)
        
    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    
    def is_square(self):
        return True if self.length == self.width else False

width = input("What is the width of the rectangle? ")
length = input("What is the length of the rectangle? ")
is_squared = ''
    
rec = Rectangle(width, length)
if not rec.is_square():
    is_squared = "not "

print(f"The area of the rectangle is {rec.area()}")
print(f"The perimeter of the rectangle is {rec.perimeter()}")
print(f"The rectangle is {is_squared}squared.")