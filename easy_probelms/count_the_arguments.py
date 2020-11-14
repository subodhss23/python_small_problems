'''Create a function that returns the number of arguments it was called with.'''

def num_args(*args):
    return len(args)

print(num_args())
print(num_args("foo"))
print(num_args("foo", "bar"))
print(num_args(True, False))
print(num_args({}))