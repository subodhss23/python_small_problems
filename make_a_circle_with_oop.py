''' Your task is to create a circle constructor that creates a circle with a radius provided by
    an argument. The circles contructed must have two getters getArea() (Pir^2) and
    getPerimeter()(2PI*r) which gives both respective areas and perimeter(circumference).
'''
import math

class Circle:
    def __init__(self, r, PI=math.pi):
        self.r = r
        self.pi = PI

    def getArea(self):
        return round(self.pi * self.r ** 2)
    
    def getPerimeter(self):
        return round(self.pi * self.r * 2)


circo = Circle(20)
print(circo.getArea())
print(circo.getPerimeter())