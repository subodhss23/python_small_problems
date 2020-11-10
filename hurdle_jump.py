''' Create a function that takes an array of hurdle heights and a jumper's
    jump height, and determine whether or not the hurdle can clear all the hurdles.

    A hurdle can clear a hurdle if their jump height is greater than or equal to the hurdle height.'''

def hurdle_jump(hurdles, jump_height):
    new_hurdles = sorted(hurdles)
    return new_hurdles[-1] <= jump_height or new_hurdles == []

print(hurdle_jump([1, 2, 3, 4, 5], 5))
print(hurdle_jump([5, 5, 3, 4, 5], 3))
print(hurdle_jump([5, 4, 5, 6], 10))
print(hurdle_jump([1, 2, 1], 1))