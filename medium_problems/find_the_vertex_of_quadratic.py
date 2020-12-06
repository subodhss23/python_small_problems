''' Every quadratic curve y = a x^2 + b x + c has a vertex point: the turning point
    where the curve stops heading down and starts going up.

    Given the value a,b and c, you need to return the coordinates of the vertex.
    Return your answers rounded to 2 decimal places.'''

def find_vertex(a,b,c):
    x = -b/ (2* a)
    y = x**2 + b*x  + c
    return [x,y]


print(find_vertex(1, 0, 25))
print(find_vertex(-1, 0, 25))
print(find_vertex(1, 10, 4))
# print(find_vertex(-1,0,25))
# print(find_vertex(1,10,25))
# print(find_vertex(8, 4, 0))
# print(find_vertex(4, -200, 1000))
# print(find_vertex(1, -50, -1000))