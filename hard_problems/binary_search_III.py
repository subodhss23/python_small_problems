# Return true if the element is found else return False

def binary_search(lst, left, right, elem):
    left = lst[0]
    right = lst[len(lst)]
    return right, left


print(binary_search([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], left, right, 7))
print(binary_search([1, 11, 14, 15, 32, 64, 67, 88, 92, 94], left, right, 12))
print(binary_search([3, 6, 9, 12, 15, 18, 21, 24, 27, 30], left, right, 27))