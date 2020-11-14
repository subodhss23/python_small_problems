''' A number n is automorphic if n^2 ends in n.
    
    For example: n=5, n^2=25

    Create a function that takes a number and returns True if the number
    is automorphic, False if it isn't. '''


def is_automorphic(n):
    square = n**2
    new_str = str(square)
    return int(new_str[-len(str(n)):]) == n

print(is_automorphic(5))
print(is_automorphic(8))
print(is_automorphic(76))