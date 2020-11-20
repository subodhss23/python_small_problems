''' Create a function that takes a value as an argument and returns the type of this value.'''

def get_type(value):
   one = str(type(eval('value'))).split(' ')
   return one[1].strip(">")

print(get_type(1))
print(get_type("a"))
print(get_type(True))
print(get_type([]))
print(get_type(None))
print(get_type(0xFF))