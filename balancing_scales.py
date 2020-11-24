''' Given a list with an odd number of elements, return whether the scale will tip "left" or "right" based
    on the sum of the numbers. The scale will tip on the direction of the largest total. If both sides are 
    equal, return "balanced".'''

def scale_tip(lst):
    find_i = lst.index('I')
    one = 0
    two = 0
    for i in range(0, find_i):
        one+=lst[i]
    for i in range(find_i + 1, len(lst)):
        two+=lst[i]
    if one < two:
        return "right"
    elif one > two:
        return "left"
    elif one == two:
        return "balanced"


print(scale_tip([0, 0, "I", 1, 1]))
print(scale_tip([1, 2, 3, "I", 4, 0, 0]))
print(scale_tip([5, 5, 5, 0, "I", 10, 2, 2, 1]))