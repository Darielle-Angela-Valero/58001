#Write a Python class named Circle constructed from a radius or a diameter
#and two methods that will compute the area and the perimeter of a circle.

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
       return self.radius**2*3.14
    def perimeter(self):
        return 2*self.radius*3.14
    def display(self):
        print("Area:", self.area())
        print("Perimeter:", self.perimeter())
circle = Circle(float(input("Enter radius:")))
circle.display()



