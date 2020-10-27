''' write a function that returns True if both numbers are:
    - smaller than 0 or
    - greater than 0, or
    - exactly 0 
    
    otherwise, return False '''

def both(n1, n2):
    return n1 < 0 and n2 < 0 or n1 > 0 and n2 > 0 or n1 == 0 and n2 == 0 


print(both(6, 2))
print(both(-6, -9))
print(both(6, -2))
print(both(0, 0))