''' Create a function that takes a string and returns the middle character(s). If the word's length is odd,
    return the middle character. If the word's length is even, return the middle two characters.'''

def get_middle(str):
    if str == "":
        return ""
    else:
        if len(str) % 2 != 0:
            return str[len(str)//2]
        else:
            return str[len(str)//2 - 1] + str[len(str)//2] 
        
        


print(get_middle("test"))
print(get_middle("testing"))
print(get_middle("middle"))
print(get_middle("A"))