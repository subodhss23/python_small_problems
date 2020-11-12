# Create a function that returns the total number of parameters passed in. 

def number_args(*args):
    return len(args)

print(number_args(1,2,3,4,5))