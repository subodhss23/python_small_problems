''' You will be implementing a basic case of the map-reduce pattern in programming.
    Given a vector stored as a list of integers, find the magnitude of the vector. Use
    the standard distance formula for n-dimesnsional Cartesian coordiantes.'''

# import numpy as np
# def magnitude(lst):
#     x = np.array(lst)
#     return(np.linalg.norm(x))

import math

def magnitude(lst):
    if lst ==[]:
        return 0
    else:
        square_sum = 0
        for i in lst:
            square_sum += i ** 2
        dist = math.sqrt(square_sum)
        return dist


print(magnitude([3, 4]))
print(magnitude([0, 0, -10]))
print(magnitude([]))
print(magnitude([2, 3, 6, 1, 8] ) )