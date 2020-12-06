''' Create a function that takes an integer and outputs an n x n square solely consisting
    of the integer n.'''

# def square_patch(n):
#     outer_lst = []
#     for row in range(0, n, 1):
#         inner_lst = []
#         for column in range(0, n, 1):
#             inner_lst.append(n)
#         outer_lst.append(inner_lst)
#     return outer_lst
        
def square_patch(n):
    result = []
    for i in range(n):
        result.append([n]* 5)
    return result

print(square_patch(5))