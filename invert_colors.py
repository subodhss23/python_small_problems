''' Create a function that inverts the rgb values of a given tuple.'''

def color_invert(rgb):
    new_tuple = ()
    for i in rgb:
        new_tuple += (255 - i,)
    return new_tuple

print(color_invert((255, 255, 255)))
print(color_invert((0, 0, 0)))
print(color_invert((165, 170, 221)))