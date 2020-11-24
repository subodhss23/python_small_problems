''' How many ways are there to navigate through a grid (w * h)? 

    Suppose you're on a 4 x 6 grid, and want to go from the bottom left to the top right.
    How many different paths can you take? Avoid backtracking, you can only move right or up.

    Create a function that takes 'w'idth and 'h'eight and returns the amount of possibilities.
'''
import math
def grid_pos(lst):
    n = sum(lst)
    r = lst[0]
    s = n - r
    return math.factorial(n)/(math.factorial(r)* math.factorial(s))

print(grid_pos([1, 1]))
print(grid_pos([6, 4]))
print(grid_pos([5, 5]))