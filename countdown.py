''' create a function that takes a number as an arguement and returns a list
    of numbers counting down from this number to zero. '''


def countdown(start):
    new_arr = []
    for i in range(0, start + 1):
        new_arr.append(start - i)
    return new_arr

print(countdown(5))