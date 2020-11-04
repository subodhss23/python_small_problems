''' Return the smallest number of steps it takes to convert a string entirely into uppercase or
    entirely into lower case, whichever takes the fewest number of steps. A step consists of changing
    one character from lower to upper case, or vice versa. '''

def steps_to_convert(txt):
    counter_upper = 0
    counter_lower = 0
    for i in txt:
        if i.islower():
            counter_lower+=1
            # print(counter_lower)
        elif i.isupper():
            counter_upper+=1
            # print(counter_upper)
    if counter_upper >= counter_lower:
        return counter_lower
    elif counter_lower >= counter_upper:
        return counter_upper

print(steps_to_convert("abC"))
print(steps_to_convert("abCBA"))
print(steps_to_convert("aba"))
print(steps_to_convert("abaCCC"))