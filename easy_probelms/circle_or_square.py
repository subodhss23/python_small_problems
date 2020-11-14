''' Given the radius of a circle and the area of a square, return True if
    the circumference of the circle is greater than the square's perimeter and
    False if the square's perimeter is greater than the circumference of the circle.'''

import math
def circle_or_square(rad, area):
    pi = 3.14
    circum = 2 * pi * rad
    perim = math.sqrt(area) * 4
    print(circum, perim)
    return circum > perim

print(circle_or_square(16, 625))
print(circle_or_square(5, 100))
print(circle_or_square(8, 144))