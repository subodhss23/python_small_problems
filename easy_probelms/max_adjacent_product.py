''' Given a list of integers, find the pair of adjacent elements that 
have the largest product and return the product. '''

def adjacent_product(lst):
    result = []
    for i in range(len(lst)-1):
        result.append(lst[i] * lst[i+1])
    return max(result)

print(adjacent_product([3, 6, -2, -5, 7, 3]))
print(adjacent_product([5, 6, -4, 2, 3, 2, -23]))
print(adjacent_product([0, -1, 1, 24, 1, -4, 8, 10]) )