''' Create a function which returns the type of triangle, given the side lengths. Return the
    following values if they match the criteria. 
    
    - No sides equal: "scalene"
    - Two sides equal: "isosceles"
    - All sides equal: "equilateral"
    - Less or more than 3 sides given: "not a triangle"
    '''

def get_triangle_type(lst):
    if len(lst) == 3:
        new_set = set(lst)
        if len(new_set) == 3:
            return 'scalene'
        elif len(new_set) == 2:
            return 'isosceles'
        elif len(new_set) == 1:
            return 'equilateral'
    return "not a triangle"

print(get_triangle_type([2, 6, 5]))
print(get_triangle_type([4, 4, 7]))
print(get_triangle_type([8, 8, 8]))
print(get_triangle_type([3, 5, 5, 2]))