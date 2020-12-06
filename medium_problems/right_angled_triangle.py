''' Given three number x, y, and z, determine whether they are the edges
    of right angled triangle. '''

def right_triangle(x, y, z):
    new_lst = sorted([x, y, z])
    for i in new_lst:
        if i <= 0:
            return False
    return new_lst[2] ** 2 == new_lst[1] ** 2 + new_lst[0] ** 2

print(right_triangle(3, 4, 5))
print(right_triangle(145, 105, 100))
print(right_triangle(70, 130, 110))
print(right_triangle(0, 4, 4))