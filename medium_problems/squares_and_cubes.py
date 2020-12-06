''' Create a function that takes a list of two numbers and checks if the sqare root of the first
    number is equal to the cube root of the second number.'''

def check_square_and_cube(lst):
    return lst[0]**1.5 == lst[1]

print(check_square_and_cube([4, 8]))
print(check_square_and_cube([16, 48]))
print(check_square_and_cube([9, 27]))
print(check_square_and_cube([25, 125]))

