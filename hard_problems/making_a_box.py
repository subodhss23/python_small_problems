''' Create a function that creates a box based on dimension n.'''

def make_box(n):
    size = n
    new_arr = []
    for i in range(size):
        print(i)
        if i == 0 or i == size - 1:
            new_arr.append("#"*(size))
        else:
            new_arr.append("#" + " "*(size - 2) + "#")
    return new_arr

print(make_box(5))
# print(make_box(3))
# print(make_box(2))
# print(make_box(1))