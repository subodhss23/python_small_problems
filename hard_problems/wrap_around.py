''' Create a function to reproduce the wrap around effect shown:'''

def wrap_around(string, offset):
    offset = offset % len(string)
    return string[offset:] + string[:offset]

print(wrap_around("Hello, World!", 2))
print(wrap_around("From what I gathered", -4))
print(wrap_around("Excelsior", 30))
print(wrap_around("Nonscience", -116))