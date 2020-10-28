''' write a function that takes coordinates of two points on a two-dimensional
    plane and retruns the length of the line segment connecting those two points. '''

import math
def line_length(dot1, dot2):
    result = (dot1[0] - dot2[0]) ** 2 + (dot1[1] - dot2[1]) ** 2
    return round(math.sqrt(result), 2)

print(line_length([15, 7], [22,11]))
print(line_length([0,0], [0, 0]))
print(line_length([0, 0], [1, 1]))