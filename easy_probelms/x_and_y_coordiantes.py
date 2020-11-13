''' Create a function that converts two lists of x- and y- cordinates into
    a list of (x, y)'''

def convert_cartesian(x, y):
    new_lst = []
    for i in range(len(x)):
        new_lst.append([x[i], y[i]])
    return new_lst

print(convert_cartesian([1, 5, 3, 3, 4], [5, 8, 9, 1, 0]) )
print(convert_cartesian([9, 8, 3], [1, 1, 1]))