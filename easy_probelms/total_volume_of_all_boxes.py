''' Given a list of boxes, create a function that returns the total volume of all
    hotse boxes combined together. A box is represented by a list with three elements:
    length, width and height.
    
    For instance,, total_volume([2, 3, 2], [6, 6, 7], [1, 2, 1])) should return
    266 since (2 x 3 x 2) + (6 x 6 x 7) + (1 x 2 x 1) = 12 + 252 + 2 = 266.
    '''

def total_volume(*boxes):
    total = 0
    for i in boxes:
        product = 1
        for j in range(len(i)):
            product*= i[j]
        total+=product
    return total

print(total_volume([4, 2, 4], [3, 3, 3], [1, 1, 2], [2, 1, 1]))
print(total_volume([2, 2, 2], [2, 1, 1]))
print(total_volume([1, 1, 1]))