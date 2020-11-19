''' Create a function(named fifth) that takes some arguements and returns the type of the fifth
    argument. In case the arguments were less than 5, return "Not enough arguments".
'''

def fifth(*args):
    if len(args) < 5:
        return 'Not enough arguments'
    else:
        return(type(args[4]))


print(fifth(1, 2, 3, 4, 5))
print(fifth("a", 2, 3, [1, 2, 3], "five"))
print(fifth())