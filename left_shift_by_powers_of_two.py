''' Write a function that mimics(without the use of <<) the left shift 
    operator and returns the result from the two given integers. '''

def shift_to_left(x, y):
    return x * 2 ** y

print(shift_to_left(5, 2))
print(shift_to_left(10, 3))
print(shift_to_left(-32, 2))
print(shift_to_left(-6, 5))