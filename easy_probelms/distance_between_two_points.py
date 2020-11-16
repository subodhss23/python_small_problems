''' In this challenge, you have to find the distance between two points
    placed on a Cartesian plane. Knowing the coordinates of both the points,
    you have to apply the Pythagorean theorem to find the distance between them. 

    Given two dictionaries a and b being the two points coordinates (x and y),
    implement a function that returns the distance between the points, rounded
    to the nearest thousandth. '''

import math
def get_distance(a, b):
    result = (a['x'] - b['x']) ** 2 + (a['y'] - b['y']) ** 2
    return round(math.sqrt(result), 3)



print(get_distance({"x": -2, "y": 1}, {"x": 4, "y": 3}) )
# print(get_distance({"x": 0, "y": 0}, {"x": 1, "y": 1}) )
# print(get_distance({"x": 10, "y": -5}, {"x": 8, "y": 16}))