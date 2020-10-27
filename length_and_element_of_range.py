''' create a function that takes a range object r, index i, and returns
    a list where the first element is the nubmer of elements in the range
    object, and the second element is the element of the range object at the given index.'''


def length_element(r, i):
    return [len(r), r[i]]

#print(length_element(range(2, 4), 0))
print(length_element(range(2, 40), 25))
# print(length_element(range(12, 15, 2), 1))
# print(length_element(range(12, 35, 4), 5))
# print(length_element(range(40, 50, 3), 2))